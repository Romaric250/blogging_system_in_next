import React from 'react';
import Link from 'next/link';
import styles from "./authlink.module.css"

const AuthLinks = () => {

    const user_auth = "not authenticated"
    return (
        <div>
            {user_auth !== "not authenticated" ? (

            <Link href="/login">
                Login
            </Link>
            ): (
<>

                        <Link href="/write">Create Blog</Link>
            
                        <span className={styles.link}>Logout</span>
                        
</>
                    
            )}
        </div>
    );
};

export default AuthLinks;