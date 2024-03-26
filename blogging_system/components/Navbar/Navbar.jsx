"use client"
import React from 'react';
import Link from 'next/link';
import { useState } from 'react';
import styles from './navbar.module.css';
import AuthLinks from '../AuthLinks/AuthLinks';
import ThemeToggle from '../ThemeToggle/ThemeToggle';


const NavLinks = () => {
    return (
        <>
                <Link href="/">Home</Link>
                <Link href="/">About</Link>
                <Link href="/">Contact</Link>
                <Link href="/">Docs</Link>
                <AuthLinks/>
         <ThemeToggle/>
        </>
    )
}


const Navbar = () => {
    return (
        <div className= {styles.container}>
        
            
            <div className={styles.logo}>
                logo here
            </div>
            
            <div className={styles.links}>
               <NavLinks/>

            </div>
            
  
        </div>
    )
}

export default Navbar