import React from 'react';
import './Header.css';

const Header: React.FC = () => {
    const scrollToSection = (id: string) => {
        const element = document.getElementById(id);
        element?.scrollIntoView({ behavior: 'smooth' });
    };

    return (
        <header className="header">
            <nav className="nav container">
                <div className="logo"> Viharahamed</div>
                <ul className="nav-menu">
                    <li><a onClick={() => scrollToSection('home')}>Home</a></li>
                    <li><a onClick={() => scrollToSection('about')}>About</a></li>
                    <li><a onClick={() => scrollToSection('experience')}>Experience</a></li>
                    <li><a onClick={() => scrollToSection('projects')}>Projects</a></li>
                    <li><a onClick={() => scrollToSection('skills')}>Skills</a></li>
                    <li><a onClick={() => scrollToSection('contact')}>Contact</a></li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
