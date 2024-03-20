import React from 'react'
import styles from "./card.module.css"
import Link from "next/link"
const Card = () => {
  return (
      <div className={styles.container}>
          
           
                  <div className={styles.imageContainer}>
                      
                  </div>
          <div className={styles.textContainer}>
              <div className={styles.detail}>
                  <span className={styles.date}>20.02.2024</span>
                  <span className={styles.category}>Culture</span>
              </div>

              <h2 className={styles.subtitle}>Lorem ipsum dolor sit amet.</h2>
              <p className={styles.desc}>
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus, enim sint.
              </p>


              <Link href="/">Read More</Link>
                  </div>
              
    </div>
  )
}

export default Card