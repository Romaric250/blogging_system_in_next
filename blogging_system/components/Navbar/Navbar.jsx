"use client"
import React from 'react';
import Link from 'next/link';
import { useState } from 'react';
import styles from './navbar.module.css';
import AuthLinks from '../AuthLinks/AuthLinks';
import ThemeToggle from '../ThemeToggle/ThemeToggle';

const Navbar = () => {
    return (
        <div className= {styles.container}>
            <div className={styles.social}>
                <li>
                    facebook
                </li>
                <li>
                    linkedn
                </li>
                <li>
                    twitter
                </li>
                
            </div>
            
            <div className={styles.logo}>
                logo here
            </div>
            
            <div className={styles.links}>
                <ThemeToggle/>
                <Link href="/">Home</Link>
                <Link href="/">About</Link>
                <Link href="/">Contact</Link>
                <Link href="/">Docs</Link>
                <AuthLinks/>

            </div>
            
  
        </div>
    )
}

export default Navbar