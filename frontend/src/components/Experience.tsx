import React, { useEffect, useState } from 'react';
import type { Experience as ExperienceType } from '../types';
import { apiService } from '../services/api';
import DataAnalyticsIllustration from './DataAnalyticsIllustration';
import './Experience.css';

const Experience: React.FC = () => {
    const [experiences, setExperiences] = useState<ExperienceType[]>([]);

    useEffect(() => {
        apiService.getExperiences().then(setExperiences).catch(console.error);
    }, []);

    return (
        <section id="experience" className="experience section">
            <div className="container">
                <h2 className="section-title text-center">Work Experience</h2>
                <div className="experience-wrapper">
                    <div className="timeline">
                        {experiences.map((exp, index) => (
                            <div key={exp.id} className="timeline-item" style={{ animationDelay: `${index * 0.2}s` }}>
                                <div className="timeline-content">
                                    <div className="timeline-date">
                                        {exp.start_date} - {exp.end_date || 'Present'}
                                    </div>
                                    <h3>{exp.position}</h3>
                                    <h4 className="company">{exp.company}</h4>
                                    {exp.description && <p>{exp.description}</p>}
                                    {exp.technologies && exp.technologies.length > 0 && (
                                        <div className="tech-tags">
                                            {exp.technologies.map((tech, i) => (
                                                <span key={`${exp.id}-tech-${i}`} className="tech-tag">{tech}</span>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            </div>
                        ))}
                    </div>
                    <div className="illustration-container">
                        <DataAnalyticsIllustration />
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Experience;
