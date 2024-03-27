
import styles from "./feautures.module.css"
import Image from "next/image"

const Feautures = () => {
  return (
      <div className={styles.container}>
          <h1 className={styles.title}>
              Discover some of my blog posts
          </h1>

          <div className={styles.post}>
              <div className={styles.imgContainer}>
                  <Image src="/romaric.jpg" width={300} height={300}/>
                
              </div>
              <div className={styles.textContainer}>
                <h1 className={styles.postTitle}>My ALXSE Software Engineering Journey</h1>
                <p className={styles.postdescription}>
In just one year, my journey as a software engineer, has been nothing short of transformative. With unwavering determination, I immersed myself in the world of coding, algorithms, and problem-solving. I embraced challenges, honing my skills through intense study and hands-on experience. Python, C,Typscript and JavaScript became my allies as I delved deeper into programming fundamentals.It has been a mind blowing opportunity to fall into this  life changing program
"""</p>
                  
              <button className={styles.button}>Read more</button>
              </div>
          </div>
          
          Feautures
    
    
    
    
    
      </div>
  )
}

export default Feautures