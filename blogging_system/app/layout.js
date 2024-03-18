import React from "react"
import { Inter } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar/Navbar";
import Footer from "@/components/Footer/Footer";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "A blogging System in Nextjs",
  description: "Created by Romaric Lonfonyuy",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="container">
          <div className="wrapper">
<Navbar/>
            {children}
           <Footer/>
          </div>
        </div> 
      </body>
    </html>
  );
}
