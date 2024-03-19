"use client"
import { createContext, useEffect, useState} from "react";

export const ThemeContext = createContext();

const GetThemFromLocalStorage = () => {
    if (typeof window !== 'undefined' && window.localStorage) {
        const value = window.localStorage.getItem("theme");
        return value || "light";
    }
}

export const ThemeContextProvider = ({ children }) => {

    const [theme, setTheme] = useState(() => {
        return GetThemFromLocalStorage();
    });

    useEffect(() => {
        localStorage.setItem("theme", theme)

    },[theme])
    const toggle = () => {
        setTheme(theme == "light" ? "dark": "light")
    }

    




    return <ThemeContext.Provider value={{theme, toggle}}> {children }</ThemeContext.Provider>
}