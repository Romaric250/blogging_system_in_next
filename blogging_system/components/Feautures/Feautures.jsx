
import styles from "./feautures.module.css"

const Feautures = () => {
  return (
      <div className={styles.container}>
          <h1 className={styles.title}>
              Discover some of my blog posts
          </h1>

          <div className={styles.post}>
              <div className={styles.imgContainer}>
                  img
                
              </div>
              <div className={styles.textContainer}>
                <h1 className={styles.postTitle}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo, consequatur!</h1>
                <p className={styles.postdescription}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi excepturi maxime repellendus aliquid rerum! Accusantium similique voluptatibus aperiam sit. Qui perspiciatis esse, ratione reiciendis facilis rerum tempora debitis mollitia modi quod autem dicta, voluptatibus quibusdam magnam dolorum quasi consequuntur placeat aspernatur dolores non exercitationem. Dolorum doloremque quod dolores provident et!</p>
                  
              <button className={styles.button}>Read more</button>
              </div>
          </div>
          
          Feautures
    
    
    
    
    
      </div>
  )
}

export default Feautures