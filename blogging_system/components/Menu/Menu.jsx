import React from 'react'
import styles from "./menu.module.css"
import Link from "next/link"

const Menu = () => {
  return (
      <div className={styles.container}>
          <h2 className={styles.subtitle}>{"whats is hot"}</h2>
          
          <h1 className={styles.title}>Most Popular</h1>

          <div className={styles.items}>
              <Link href="/" className={styles.item}>
                  <div className={styles.image}>
                      
                  </div>
                  <div className={styles.textContainer}>
                      <span className={`${styles.category} ${styles.travel}`}>Travel</span>
                      <h3>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam, aspernatur?</h3>   

                      <div className={styles.detail}>
                          <span className={styles.username}> Romaric Lonfonyuy</span>
                          <span className={styles.date}>20.03.2024</span>
                      </div>                      
                  </div>
              
                  
              
              </Link>
              <Link href="/" className={styles.item}>
                  <div className={styles.image}>
                      
                  </div>
                  <div className={styles.textContainer}>
                      <span className={`${styles.category} ${styles.travel}`}>Travel</span>
                      <h3>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam, aspernatur?</h3>   

                      <div className={styles.detail}>
                          <span className={styles.username}> Romaric Lonfonyuy</span>
                          <span className={styles.date}>20.03.2024</span>
                      </div>                      
                  </div>
              
                  
              
              </Link>
              <Link href="/" className={styles.item}>
                  <div className={styles.image}>
                     
                  </div>
                  <div className={styles.textContainer}>
                      <span className={`${styles.category} ${styles.travel}`}>Travel</span>
                      <h3>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam, aspernatur?</h3>   

                      <div className={styles.detail}>
                          <span className={styles.username}> Romaric Lonfonyuy</span>
                          <span className={styles.date}>20.03.2024</span>
                      </div>                      
                  </div>
              
                  
              
              </Link>
              <Link href="/" className={styles.item}>
                  <div className={styles.image}>
                      
                  </div>
                  <div className={styles.textContainer}>
                      <span className={`${styles.category} ${styles.travel}`}>Travel</span>
                      <h3>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam, aspernatur?</h3>   

                      <div className={styles.detail}>
                          <span className={styles.username}> Romaric Lonfonyuy</span>
                          <span className={styles.date}>20.03.2024</span>
                      </div>                      
                  </div>
              
                  
              
              </Link>
              
              
          </div>

    </div>
  )
}

export default Menu