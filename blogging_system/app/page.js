import CategoryList from "../components/CategoryList/CategoryList"

import Feautures from "../components/Feautures/Feautures";
import Image from "next/image";
import styles from "./main.module.css"
import CardList from "../components/CardList/CardList";
import Menu from "../components/Menu/Menu";
import Pagination from "../components/Pagination/Pagination";

export default function Home({searchParams}) {

  const page = parseInt(searchParams.page) || 1;
  return (
    <div>
      
      <Feautures/>
      <CategoryList/>

      <div className={styles.content}>
        <div className={styles.right_content}>

        <CardList page={page} />
        </div>
        < div className={styles.left_content}>
          <Menu/>
        </div>
      </div>

      
      
    </div>

  );
}
