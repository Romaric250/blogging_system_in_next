import React from "react";
import styles from "./footer.module.css";
import Image from "next/image";
import Link from "next/link";

const Footer = () => {
  return (
    <div className={styles.container}>
      <div className={styles.info}>
        <div className={styles.logo}>
          <h1 className={styles.logoText}> <a href="https://github.com/Romaric250">Romaric Lonfonyuy</a> </h1>
        </div>
        <p className={styles.desc}>
         <strong> <a href="https://github.com/Romaric250/blogging_system_in_next/" target="__blank">Source Code</a></strong>
        </p>
      </div>
      <div className={styles.links}>
        <div className={styles.list}>
          <span className={styles.listTitle}>Links</span>
          <Link href="/">Homepage</Link>
          <Link href="/">Blog</Link>
          <Link href="/">About</Link>
          <Link href="/">Contact</Link>
        </div>
        <div className={styles.list}>
          <span className={styles.listTitle}>Tags</span>
          <Link href="/">coding</Link>
          <Link href="/">Artificial intelligence</Link>
          <Link href="/">Competitions</Link>
          <Link href="/">Cultural</Link>
        </div>
        <div className={styles.list}>
          <span className={styles.listTitle}>Social</span>
          <Link href="/">Competitions</Link>
          <Link href="/">others</Link>

        </div>
      </div>
    </div>
  );
};

export default Footer;