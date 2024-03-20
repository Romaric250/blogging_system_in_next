import Card from "../Card/Card"
import styles from "./cardlist.module.css"

const CardList = () => {
  return (
      <div className={styles.container}>
          <h2 className={styles.title}> Recent Post</h2>
          <div className={styles.posts}>
              
                  
            <Card />
            <Card />
            <Card />
            <Card />
            <Card />
          </div>
    </div>
  )
}

export default CardList