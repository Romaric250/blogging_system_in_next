import React from 'react';
import styles from './about.module.css';
import Image from "next/image"
import { Linkedin, Github, Mail } from 'lucide-react'; // Import the icons

const AboutPage = () => {
    return (
        <div className={styles.container}>

            <div className={styles.main_container}>
                <div className={styles.image}>
                    <Image src="/romaric.jpg" alt="romaric" width={300} height={300}/>
                </div>

                <div className={styles.text}>
                    <h1>Hi, I'm <strong>Romaric Lonfonyuy</strong></h1>
                    <p>
                        I'm a full-stack developer and I love building web applications. I'm currently learning Next.js and I'm excited to see what I can build with it!
                    </p>
                    <p>
                        I have experience working with various technologies such as React, Node.js, and MongoDB. I enjoy solving complex problems and creating efficient and scalable solutions.
                    </p>
                    <p>
                        In my free time, I like to contribute to open-source projects and explore new technologies. I'm passionate about continuous learning and staying up-to-date with the latest trends in web development.
                    </p>
                    <div className={styles.socialLinks}>
                        <a href="https://www.linkedin.com/your-linkedin-profile" target="_blank" rel="noopener noreferrer">
                            <Linkedin size={40} />
                        </a>
                        <a href="https://github.com/Romaric250/" target="_blank" rel="noopener noreferrer">
                            <Github size={40} />
                        </a>
                        <a href="mailto:lonfonyuyromaric.com">
                            <Mail size={40} />
                        </a>
                    </div>
                </div>
            </div>

            <h2 className={styles.contactme}>Contact Me</h2>
            <form className={styles.contactForm}>
                <input type="text" placeholder="Name" />
                <input type="email" placeholder="Email" />
                <textarea placeholder="Message"></textarea>
                <button type="submit">Send Message</button>
            </form>
        </div>
    );
};

export default AboutPage;