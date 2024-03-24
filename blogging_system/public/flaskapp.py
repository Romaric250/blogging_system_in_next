from flask import Flask, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_cors import CORS
from bson import ObjectId
app = Flask(__name__)
app.secret_key = "deplan@dev"

CORS(app)
# Replace <connection_string> and <database_name> with your actual values
client = MongoClient("mongodb+srv://philballer41:$User_2001$@master.crhkpcw.mongodb.net/?retryWrites=true&w=majority&appName=Master")

db = client.deplan

print("Connected to the database successfully!")


@app.route("/", methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the Deplan API'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    if email and password and request.method == "POST":
        user = db.user.find_one({'email': email})

        if user and check_password_hash(user['password'], password):
            # Login successful
            message = {
                'status': 200,
                'message': 'Login successful',
                'email': user['email'],
                'id': str(user['_id'])
            }
            return jsonify(message), 200
        else:
            # Invalid credentials
            message = {
                'status': 401,
                'message': 'email or password incorrect'
            }
            return jsonify(message), 401
    else:
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    return jsonify(message), 404



@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    email = data['email']
    pwd = data['password']

    if email and pwd and request.method == "POST":
        hash_pwd = generate_password_hash(pwd)
        user_data = {'email': email, 'password': hash_pwd}
        db.user.insert_one(user_data)

        message = {
            'status': 200,
            'message': 'User added successfully'
        }
        return jsonify(message), 200
    else:
        return not_found()

@app.route('/update/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    pwd = data.get('password')

    if email and pwd and name and request.method == "PUT":
        hash_pwd = generate_password_hash(pwd)
        user_data = {'name': name, 'email': email, 'password': hash_pwd}

        result = db.user.update_one({'_id': user_id}, {'$set': user_data})

        if result.modified_count > 0:
            message = {
                'status': 200,
                'message': 'User updated successfully'
            }
        else:
            message = {
                'status': 404,
                'message': 'User not found'
            }

        return jsonify(message), 200
    else:
        return not_found()


@app.route('/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = db.user.delete_one({'_id': user_id})

    if result.deleted_count > 0:
        message = {
            'status': 200,
            'message': 'User deleted successfully'
        }
    else:
        message = {
            'status': 404,
            'message': 'User not found'
        }

    return jsonify(message), 200

@app.route('/get_users', methods=['GET'])
def get_users():
    users = db.user.find({}, {'_id': 1, 'name': 1, 'email': 1, 'password': 1})

    user_list = []
    for user in users:
        user['_id'] = str(user['_id'])
        user_list.append(user)

    return jsonify(user_list), 200

# from here we hae all the journal routes



#working
@app.route('/add_journal/<user_id>', methods=['POST'])
def add_journal(user_id):

    data = request.json
    name = data['name']
    summary = data['summary']
    initial_balance = data.get('initial_balance', 0)  # Default to 0 if not provided
    account_balance = data.get('account_balance', 0)  # Default to 0 if not provided

    if user_id and name and summary and request.method == "POST":
        user = db.user.find_one({'_id': ObjectId(user_id)})
        if user:
            journal_data = {
                'user_id': user_id,
                'name': name,
                'summary': summary,
                'account_balance': account_balance,
                'initial_balance': initial_balance,
            }
            result = db.journals.insert_one(journal_data)

            message = {
                'status': 200,
                'message': 'Journal added successfully',
                'journal_id': str(result.inserted_id)
            }
        else:
            message = {
                'status': 404,
                'message': 'User not found'
            }

        return jsonify(message), 200
    else:
        return not_found()
#working
@app.route('/get_journal/<journal_id>', methods=['GET'])
def get_journal(journal_id):
    journal = db.journals.find_one({'_id': ObjectId(journal_id)})
    if journal:
        response = {
            'status': 200,
            'data': {
                'id': str(journal['_id']),
                'name': journal['name'],
                'summary': journal['summary'],
                'account_balance': journal['account_balance'] if 'account_balance' in journal else 0,
                'initial_balance': journal['initial_balance'] if 'initial_balance' in journal else 0
            }
        }
    else:
        response = {
            'status': 404,
            'message': 'Journal not found'
        }
    return jsonify(response)


#working
@app.route('/update_journal/<journal_id>', methods=['PUT'])
def update_journal(journal_id):
    data = request.json
    name = data.get('name')
    summary = data.get('summary')
    account_balance = data.get('account_balance')

    if name and summary and request.method == "PUT":
        result = db.journals.update_one({'_id': ObjectId(journal_id)}, {'$set': {'name': name, 'summary': summary, "account_balance": account_balance if account_balance else 0}})

        if result.modified_count > 0:
            message = {
                'status': 200,
                'message': 'Journal updated successfully'
            }
        else:
            message = {
                'status': 404,
                'message': 'Journal not found'
            }

        return jsonify(message), 200
    else:
        return not_found()

#working
@app.route('/delete_journal/<journal_id>', methods=['DELETE'])
def delete_journal(journal_id):
    result = db.journals.delete_one({'_id': ObjectId(journal_id)})

    if result.deleted_count > 0:
        message = {
            'status': 200,
            'message': 'Journal deleted successfully'
        }
    else:
        message = {
            'status': 404,
            'message': 'Journal not found'
        }

    return jsonify(message), 200

# working
@app.route('/view_journals/<user_id>', methods=['GET'])
def view_journals(user_id):
    journals = db.journals.find({'user_id': user_id}, {'user_id': 0})

    journal_list = []
    for journal in journals:
        journal['_id'] = str(journal['_id'])
        journal_list.append(journal)

    return jsonify(journal_list), 200

# not important

# @app.route('/get_all_journal_data',methods=['GET'])
# def get_journal_data():
#     journal_data = db.journal_description.find({},{'_id':1,'asset':1,'direction':1,'position':1,'size':1,
#                                                    'risk':1,
#                                                    'realised':1,'profit_in_r':1,'profit_in_dollar':1,
#                                                    'setup':1,
#                                                    'result':1
#                                                    })
#     journal_data_list = []

#     for data in journal_data:
#         data['_id'] = str(data['_id'])
#         journal_data_list.append(data)

#     return jsonify(journal_data_list)

#working
@app.route('/get_journal_description/<journal_description_id>', methods=['GET'])
def get_journal_description(journal_description_id):
    journal_data = db.journal_description.find_one(
        {'_id': ObjectId(journal_description_id)},
        {
            'asset': 1,
            'direction': 1,
            'risk_in_pips': 1,
            'profit_in_pips': 1,
            'lot_size': 1,
            'profit_in_r': 1,
            'profit_in_dollar': 1,
            'setup': 1,
            'result': 1
        }
    )

    if journal_data:
        descriptionlist = []
        journal_data['_id'] = str(journal_data['_id'])
        descriptionlist.append(journal_data)

        return jsonify(descriptionlist)
    else:
        return not_found()

#works
@app.route('/add_journal_description/<journal_id>', methods=['POST'])
def add_journal_description(journal_id):
    data = request.json
    asset = data.get('asset')
    direction = data.get('direction')
    risk_in_pips = data.get('risk_in_pips')
    profit_in_pips = data.get('profit_in_pips')
    lot_size = data.get('lot_size')
    profit_in_r = data.get('profit_in_r')
    profit_in_dollar = data.get('profit_in_dollar')
    setup = data.get('setup')
    result = data.get('result')

    if journal_id and asset and direction and risk_in_pips and lot_size and request.method == "POST":
        journal_data = db.journals.find_one({'_id': ObjectId(journal_id)})

        if journal_data:
            account_balance = journal_data.get('account_balance', 0)

            # Updates account balance
            if profit_in_dollar is not None:
                if account_balance > 0:
                    account_balance += profit_in_dollar
                else:
                    account_balance += -profit_in_dollar

            # Update the account balance in the journal
            db.journals.update_one(
                {'_id': ObjectId(journal_id)},
                {'$set': {'account_balance': account_balance}}
            )

            journal_description_data = {
                'journal_id': journal_id,
                'datecreated': datetime.now(),
                'asset': asset,
                'direction': direction,
                'risk_in_pips': risk_in_pips,
                'profit_in_pips': profit_in_pips,
                'lot_size': lot_size,
                'profit_in_r': profit_in_r,
                'profit_in_dollar': profit_in_dollar,
                'setup': setup,
                'result': result,
            }
            result = db.journal_description.insert_one(journal_description_data)

            message = {
                'status': 200,
                'message': 'Journal description added successfully',
                'journal_description_id': str(result.inserted_id)
            }
            
        else:
            message = {
                'status': 404,
                'message': 'Journal not found'
            }

        return jsonify(message), 200
    else:
        return not_found()


#working
@app.route('/update_journal_description/<journal_description_id>', methods=['PUT'])
def update_journal_description(journal_description_id):
    data = request.json
    asset = data.get('asset')
    direction = data.get('direction')
    risk_in_pips = data.get('risk_in_pips')
    profit_in_pips = data.get('profit_in_pips')
    lot_size = data.get('lot_size')
    profit_in_r = data.get('profit_in_r')
    profit_in_dollar = data.get('profit_in_dollar')
    setup = data.get('setup')
    result = data.get('result')

    if journal_description_id and request.method == "PUT":
        journal_description_data = db.journal_description.find_one({'_id': ObjectId(journal_description_id)})

        if journal_description_data:
            update_data = {k: v for k, v in data.items() if v is not None}

            db.journal_description.update_one(
                {'_id': ObjectId(journal_description_id)},
                {'$set': update_data}
            )

            # If profit_in_dollar is updated, update the account balance in the associated journal
            if 'profit_in_dollar' in update_data:
                journal_data = db.journals.find_one({'_id': ObjectId(journal_description_data['journal_id'])})
                if journal_data:
                    account_balance = journal_data.get('account_balance', 0)
                    if account_balance > 0:
                        account_balance += update_data['profit_in_dollar']
                    else:
                        account_balance += -update_data['profit_in_dollar']

                    db.journals.update_one(
                        {'_id': ObjectId(journal_description_data['journal_id'])},
                        {'$set': {'account_balance': account_balance}}
                    )
                    
            message = {
                'status': 200,
                'message': 'Journal description updated successfully',
            }
        else:
            message = {
                'status': 404,
                'message': 'Journal description not found'
            }

        return jsonify(message), 200
    else:
        return not_found()


#working
@app.route('/delete_journal_description/<journal_description_id>', methods=['DELETE'])
def delete_journal_description(journal_description_id):
    journal_description = db.journal_description.find_one({'_id': ObjectId(journal_description_id)})

    if journal_description:
        profit_in_dollar = journal_description.get('profit_in_dollar', 0)
        journal_id = journal_description.get('journal_id')

        
        journal = db.journals.find_one({'_id': ObjectId(journal_id)})
        if journal:
            new_account_balance = journal.get('account_balance', 0) - profit_in_dollar
            db.journals.update_one({'_id': ObjectId(journal_id)}, {'$set': {'account_balance': new_account_balance}})

        
        result = db.journal_description.delete_one({'_id': ObjectId(journal_description_id)})

        if result.deleted_count > 0:
            message = {
                'status': 200,
                'message': 'Journal description deleted successfully'
            }
        else:
            message = {
                'status': 404,
                'message': 'Journal description not found'
            }
    else:
        message = {
            'status': 404,
            'message': 'Journal description not found'
        }

    return jsonify(message), 200
#working
@app.route('/view_journal_descriptions/<journal_id>', methods=['GET'])
def view_journal_descriptions(journal_id):
    journal_descriptions = db.journal_description.find({'journal_id': journal_id}, {'journal_id': 0})

    journal_description_list = []
    for journal_description in journal_descriptions:
        journal_description['_id'] = str(journal_description['_id'])
        journal_description_list.append(journal_description)

    return jsonify(journal_description_list), 200


@app.route('/get_journal_trades/<journal_id>', methods=['GET'])
def get_total_journals(journal_id):
    journal_descriptions = db.journal_description.find({'journal_id': journal_id}, {'journal_id': 0})

    total_journal = 0
    journal_description_list = []
    for journal_description in journal_descriptions:
        journal_description['_id'] = str(journal_description['_id'])
        total_journal = total_journal + 1

    return jsonify(total_journal), 200



@app.route('/get_profit_in_r/<journal_id>', methods=['GET'])
def get_journal_profit_in_r(journal_id):

#not that for this to work, the profit_in_r must be in a number format
    journal_descriptions = db.journal_description.find({'journal_id': journal_id}, {'journal_id': 0})

    journal_description_list = []
    for journal_description in journal_descriptions:
        journal_description['_id'] = str(journal_description['_id'])
        journal_description_list.append(journal_description) 

    journal_profit = []
    for journal in journal_description_list:
        if journal['profit_in_r'] is not None:
            journal_profit.append(journal['profit_in_r'])
        else:
            journal_profit.append(0)

        total_profit = sum(journal_profit)



    return jsonify(total_profit), 200
    

@app.route('/stats/<journal_id>', methods=['GET'])
def get_journal_stats(journal_id):
    if journal_id and request.method == "GET":
        journal_data = db.journals.find_one({'_id': ObjectId(journal_id)})
        #print(journal_data)
        journal_description_data = list(db.journal_description.find({'journal_id': journal_id}))
        #print(journal_description_data)
        if journal_data:
            initial_balance = journal_data.get('initial_balance', 0)
            most_recent_trade_account_balance = journal_data.get('account_balance', 0)

            total_profit = most_recent_trade_account_balance - initial_balance
            total_trades = len(journal_description_data)
            total_growth = ((most_recent_trade_account_balance - initial_balance) / initial_balance) * 100 if initial_balance != 0 else 0
            total_profit_in_r = sum([trade.get('profit_in_r', 0) for trade in journal_description_data])
            total_losses = len([trade for trade in journal_description_data if trade.get('profit_in_dollar', 0) < 0])
            total_wins = len([trade for trade in journal_description_data if trade.get('profit_in_dollar', 0) > 0])

            stats = {
                'total_profit': total_profit,
                'total_trades': total_trades,
                'total_growth': total_growth,
                'total_profit_in_r': total_profit_in_r,
                'total_losses': total_losses,
                'total_wins': total_wins
            }

            return jsonify(stats), 200
        else:
            return not_found()
    else:
        return not_found()

# returns the stats of the dashboard
@app.route('/stats_dashboard/<user_id>', methods=['GET'])
def get_dashboard_stats(user_id):
    if user_id and request.method == "GET":
        user_journals = list(db.journals.find({'user_id': user_id}))
        user_journal_ids = [str(journal['_id']) for journal in user_journals]

        total_balance = sum([journal.get('account_balance', 0) for journal in user_journals])

        total_trades = sum([len(list(db.journal_description.find({'journal_id': journal_id}))) for journal_id in user_journal_ids])

        total_growth = sum([((journal.get('account_balance', 0) - journal.get('initial_balance', 0)) // journal.get('initial_balance', 1)) * 1 for journal in user_journals]) // len(user_journals) if user_journals else 0
        print(total_growth)
        
        total_profit_in_r = sum([sum([trade.get('profit_in_r', 0) for trade in list(db.journal_description.find({'journal_id': journal_id}))]) for journal_id in user_journal_ids])

        total_profit = sum([(journal.get('account_balance', 0) - journal.get('initial_balance', 0)) for journal in user_journals])

        total_wins = sum([len([trade for trade in list(db.journal_description.find({'journal_id': journal_id})) if trade.get('profit_in_dollar', 0) > 0]) for journal_id in user_journal_ids])

        total_losses = sum([len([trade for trade in list(db.journal_description.find({'journal_id': journal_id})) if trade.get('profit_in_dollar', 0) < 0]) for journal_id in user_journal_ids])

        stats = {
            'total_balance': total_balance,
            'total_trades': total_trades,
            'total_growth': total_growth,
            'total_profit_in_r': total_profit_in_r,
            'total_profit': total_profit,
            'total_wins': total_wins,
            'total_losses': total_losses
        }

        return jsonify(stats), 200
    else:
        return not_found()
# @app.route('/get_journal_profit/<journal_id>', methods=['GET'])
# def get_journal_profit(journal_id):
    
#     journal = db.journals.find_one({'_id': ObjectId(journal_id)})

#     if journal:
        
#         initial_balance_entry = db.journal_description.find_one(
#             {'journal_id': journal_id},
#             sort=[('datecreated', 1)]
#         )
#         final_balance_entry = db.journal_description.find_one(
#             {'journal_id': journal_id},
#             sort=[('datecreated', -1)]
#         )

#         if initial_balance_entry and final_balance_entry:
#             initial_balance = initial_balance_entry['account_balance']
#             final_balance = final_balance_entry['account_balance']

           
#             profit = final_balance - initial_balance
#             return jsonify({'profit': profit}), 200
#         else:
#             return jsonify({'message': 'No journal entries found'}), 404
#     else:
#         return jsonify({'message': 'Journal not found'}), 404


# @app.route('/get_journal_growth/<journal_id>', methods=['GET'])
# def get_journal_growth(journal_id):
#     # Find the journal
#     journal = db.journals.find_one({'_id': ObjectId(journal_id)})

#     if journal:
#         # Find the initial and final account balances
#         initial_balance_entry = db.journal_description.find_one(
#             {'journal_id': journal_id},
#             sort=[('datecreated', 1)]
#         )
#         final_balance_entry = db.journal_description.find_one(
#             {'journal_id': journal_id},
#             sort=[('datecreated', -1)]
#         )

#         if initial_balance_entry and final_balance_entry:
#             initial_balance = initial_balance_entry['account_balance']
#             final_balance = final_balance_entry['account_balance']

#             # Calculate and return the growth
#             if initial_balance != 0:
#                 growth = ((final_balance - initial_balance) / initial_balance) * 100
#             else:
#                 growth = 0

#             return jsonify({'growth': growth}), 200
#         else:
#             return jsonify({'message': 'No journal entries found'}), 404
#     else:
#         return jsonify({'message': 'Journal not found'}), 404


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Resource not found: ' + request.url,
    }
    return jsonify(message), 404


if __name__ == "__main__":
    app.run(debug=True,)