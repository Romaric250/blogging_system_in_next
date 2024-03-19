import React from "react"
import { Inter } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar/Navbar";
import Footer from "@/components/Footer/Footer";
import  ThemeProvider  from "@/src/providers/ThemeProvider";
import { ThemeContextProvider } from "@/src/context/ThemeContext";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "A blogging System in Nextjs",
  description: "Created by Romaric Lonfonyuy",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <ThemeContextProvider>
          <ThemeProvider>

        <div className="container">
          <div className="wrapper">
<Navbar/>
            {children}
           <Footer/>
          </div>
        </div> 
          </ThemeProvider>
          

        </ThemeContextProvider>
      </body>
    </html>
  );
}
