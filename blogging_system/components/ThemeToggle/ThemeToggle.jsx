"use client"
import { useContext } from "react";
import styles from "./toggle.module.css";
import Image from "next/image"
import { ThemeContext } from "@/src/context/ThemeContext";

const ThemeToggle = () => {

    const { theme,toggle } = useContext(ThemeContext)
    console.log(theme)
    return (
        
        <div className={styles.container} onClick={toggle} style={theme === "dark" ? { left:1,background:"white"}:{right:1, background:"#0f172a"} }>
            
            <Image src="/sun.png" alt="sun" width={15} height={15}  />
            <div className={styles.ball} style = {theme === "dark" ? { left:0,background:"#0f172a"}:{right:0, background:"white"} }></div>
            <Image src="/moon.png" alt="moon" width={15} height={15} />
            


            
        </div>
    )
}


export default ThemeToggle