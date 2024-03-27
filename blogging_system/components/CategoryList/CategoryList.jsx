
import React from 'react'
import Link from 'next/link'
import styles from "./category.module.css"


// const Category = () => {
//   return (
//     <>
    
//     </>
//   )
// }




const CategoryList = () => {
  return (
    <div className={styles.container}>
<h2 className={styles.title}> Most Popular Blog Categories</h2>
      
        <div className={styles.categories}>
          <Link href="/blog?cat = style" className={`${styles.category} ${styles.style}`}>
            <div className={styles.image}>

            </div>

            Coding
          
          </Link>
          <Link href="/blog?cat = style" className={`${styles.category} ${styles.style}`}>
            <div className={styles.image}>

            </div>

            Competitions
          
          </Link>
          <Link href="/blog?cat = style" className={`${styles.category} ${styles.style}`}>
            <div className={styles.image}>

            </div>

            Programs
          
          </Link>
          <Link href="/blog?cat = style" className={`${styles.category} ${styles.style}`}>
            <div className={styles.image}>

            </div>

            Scholarships
          
          </Link>
          <Link href="/blog?cat = style" className={`${styles.category} ${styles.style}`}>
            <div className={styles.image}>

            </div>

            Others
          
          </Link>
        </div> 

    </div>
  )
}

export default CategoryList