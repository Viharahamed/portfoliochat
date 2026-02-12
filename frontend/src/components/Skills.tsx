import React from 'react';
import {
    FaHtml5,
    FaCss3Alt,
    FaReact,
    FaNodeJs,
    FaNpm,
    FaJava,
    FaPython,
    FaBootstrap
} from 'react-icons/fa';
import {
    SiJavascript,
    SiMongodb,
    SiMysql
} from 'react-icons/si';
import { BiData } from 'react-icons/bi';
import './Skills.css';

// Technology icon mapping
const techIcons: Record<string, React.ReactNode> = {
    'HTML': <FaHtml5 />,
    'CSS': <FaCss3Alt />,
    'JavaScript': <SiJavascript />,
    'React.js': <FaReact />,
    'Node.js': <FaNodeJs />,
    'Express.js': <FaNodeJs />,
    'NPM': <FaNpm />,
    'SQL': <SiMysql />,
    'MongoDB': <SiMongodb />,
    'Java': <FaJava />,
    'C': <BiData />,
    'Bootstrap': <FaBootstrap />,
    'Python': <FaPython />
};

// Flatten all technologies for display
const technologies = [
    { name: 'HTML', label: 'html-5' },
    { name: 'CSS', label: 'css3' },
    { name: 'JavaScript', label: 'JavaScript' },
    { name: 'React.js', label: 'reactjs' },
    { name: 'Node.js', label: 'nodejs' },
    { name: 'NPM', label: 'npm' },
    { name: 'SQL', label: 'sql-database' },
    { name: 'Java', label: 'java' },
    { name: 'Python', label: 'python' },
    { name: 'Bootstrap', label: 'bootstrap' }
];

const Skills: React.FC = () => {
    return (
        <section id="skills" className="skills section">
            <div className="container">
                <h2 className="skills-main-title">What I do</h2>
                <p className="skills-subtitle">
                    CRAZY FULL STACK DEVELOPER WHO WANTS TO EXPLORE EVERY TECH STACK
                </p>

                <div className="tech-icons-grid">
                    {technologies.map((tech, index) => (
                        <div
                            key={tech.name}
                            className="tech-icon-item"
                            style={{ animationDelay: `${index * 0.1}s` }}
                        >
                            <div className="tech-icon">
                                {techIcons[tech.name] || <BiData />}
                            </div>
                            <p className="tech-label">{tech.label}</p>
                        </div>
                    ))}
                </div>

                <div className="skills-description">
                    <span className="lightning-icon">⚡</span>
                    <p>
                        Develop highly interactive Front end / User Interfaces for your web and mobile applications
                    </p>
                </div>
            </div>
        </section>
    );
};

export default Skills;
