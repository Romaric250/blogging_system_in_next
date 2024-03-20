
import CategoryList from "@/components/CategoryList/CategoryList";
import Feautures from "@/components/Feautures/Feautures";
import Image from "next/image";
import styles from "./main.module.css"
import CardList from "@/components/CardList/CardList";

export default function Home() {
  return (
    <div>
      
      <Feautures/>
      <CategoryList/>

      <div className={styles.content}>

        <CardList />
        <div>
          Menue
        </div>
      </div>

      
      
    </div>

  );
}
