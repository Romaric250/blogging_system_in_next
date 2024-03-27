// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = { 
  apiKey: process.env.FIREBASE,
  authDomain: "blogging-system-96502.firebaseapp.com",
  projectId: "blogging-system-96502",
  storageBucket: "blogging-system-96502.appspot.com",
  messagingSenderId: "189230224164",
  appId: "1:189230224164:web:92dd580040d2af2211d9b1"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);