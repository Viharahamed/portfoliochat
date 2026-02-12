import React, { useEffect, useState } from 'react';
import type { Profile } from '../types';
import { apiService } from '../services/api';
import { FaGithub, FaLinkedin, FaEnvelope } from 'react-icons/fa';
import './Contact.css';

const Contact: React.FC = () => {
    const [profile, setProfile] = useState<Profile | null>(null);

    useEffect(() => {
        apiService.getProfile().then(setProfile).catch(console.error);
    }, []);

    return (
        <section id="contact" className="contact section">
            <div className="container">
                <div className="contact-layout">
                    {/* Left Side - Contact Info */}
                    <div className="contact-info-section">
                        <h2 className="contact-title">
                            Contact Me <span className="phone-emoji">☎️</span>
                        </h2>
                        <p className="contact-subtitle">
                            DISCUSS A PROJECT OR JUST WANT TO SAY HI? MY INBOX IS OPEN FOR ALL.
                        </p>

                        {profile?.phone && (
                            <div className="contact-detail">
                                <a href={`tel:${profile.phone}`} className="contact-link">
                                    {profile.phone}
                                </a>
                            </div>
                        )}

                        {profile?.email && (
                            <div className="contact-detail">
                                <a href={`mailto:${profile.email}`} className="contact-link">
                                    {profile.email}
                                </a>
                            </div>
                        )}

                        {/* Social Icons */}
                        <div className="social-icons">
                            {profile?.github && (
                                <a
                                    href={profile.github}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="social-icon"
                                    aria-label="GitHub"
                                >
                                    <FaGithub />
                                </a>
                            )}
                            {profile?.linkedin && (
                                <a
                                    href={profile.linkedin}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="social-icon"
                                    aria-label="LinkedIn"
                                >
                                    <FaLinkedin />
                                </a>
                            )}
                            {profile?.email && (
                                <a
                                    href={`mailto:${profile.email}`}
                                    className="social-icon"
                                    aria-label="Email"
                                >
                                    <FaEnvelope />
                                </a>
                            )}
                        </div>
                    </div>

                    {/* Right Side - Email Image */}
                    <div className="contact-image-section">
                        <img
                            src="/email.svg"
                            alt="Contact illustration"
                            className="contact-image"
                        />
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Contact;
