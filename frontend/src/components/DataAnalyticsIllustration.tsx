import React from 'react';

const DataAnalyticsIllustration: React.FC = () => {
    return (
        <svg
            viewBox="0 0 800 600"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            className="analytics-illustration"
        >
            {/* Background Elements */}
            <defs>
                <linearGradient id="blueGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stopColor="#6366f1" />
                    <stop offset="100%" stopColor="#4f46e5" />
                </linearGradient>
                <linearGradient id="yellowGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stopColor="#fbbf24" />
                    <stop offset="100%" stopColor="#f59e0b" />
                </linearGradient>
            </defs>

            {/* Laptop Base */}
            <rect x="150" y="380" width="500" height="15" fill="url(#blueGradient)" rx="3" />
            <rect x="100" y="395" width="600" height="8" fill="#4338ca" opacity="0.6" rx="4" />

            {/* Main Screen */}
            <rect x="180" y="150" width="440" height="230" fill="#1e293b" rx="8" stroke="#6366f1" strokeWidth="3" />

            {/* Screen Content - Chart Lines */}
            <path d="M220 320 L280 280 L340 300 L400 250 L460 270 L520 240 L580 260"
                stroke="#fbbf24" strokeWidth="4" fill="none" strokeLinecap="round" />
            <path d="M220 340 L280 310 L340 330 L400 290 L460 310 L520 280 L580 300"
                stroke="#6366f1" strokeWidth="4" fill="none" strokeLinecap="round" />

            {/* Chart Points */}
            <circle cx="220" cy="320" r="5" fill="#fbbf24" />
            <circle cx="280" cy="280" r="5" fill="#fbbf24" />
            <circle cx="340" cy="300" r="5" fill="#fbbf24" />
            <circle cx="400" cy="250" r="5" fill="#fbbf24" />
            <circle cx="460" cy="270" r="5" fill="#fbbf24" />
            <circle cx="520" cy="240" r="5" fill="#fbbf24" />
            <circle cx="580" cy="260" r="5" fill="#fbbf24" />

            {/* Bar Chart (Left Side) */}
            <g transform="translate(50, 200)">
                <rect x="0" y="80" width="40" height="100" fill="#6366f1" rx="4" />
                <rect x="50" y="40" width="40" height="140" fill="url(#yellowGradient)" rx="4" />
                <rect x="100" y="100" width="40" height="80" fill="#6366f1" opacity="0.7" rx="4" />

                {/* Percentage Labels */}
                <text x="10" y="70" fill="#6366f1" fontSize="14" fontWeight="bold">58%</text>
                <text x="60" y="30" fill="#fbbf24" fontSize="14" fontWeight="bold">91%</text>
                <text x="110" y="90" fill="#6366f1" fontSize="14" fontWeight="bold">74%</text>
            </g>

            {/* Floating Window (Top Right) */}
            <rect x="520" y="60" width="200" height="120" fill="#1e293b" rx="8" stroke="#6366f1" strokeWidth="2" />
            <rect x="520" y="60" width="200" height="25" fill="url(#blueGradient)" rx="8" />

            {/* Window Dots */}
            <circle cx="535" cy="72" r="4" fill="#ef4444" />
            <circle cx="550" cy="72" r="4" fill="#fbbf24" />
            <circle cx="565" cy="72" r="4" fill="#22c55e" />

            {/* Data Lines in Window */}
            <line x1="540" y1="110" x2="700" y2="110" stroke="#6366f1" strokeWidth="3" />
            <line x1="540" y1="130" x2="680" y2="130" stroke="#6366f1" strokeWidth="3" opacity="0.6" />
            <line x1="540" y1="150" x2="660" y2="150" stroke="#6366f1" strokeWidth="3" opacity="0.4" />

            {/* Number Display */}
            <text x="580" y="105" fill="#fbbf24" fontSize="24" fontWeight="bold">+256</text>

            {/* Pie Chart (Bottom Left) */}
            <g transform="translate(80, 450)">
                <circle cx="0" cy="0" r="50" fill="#1e293b" stroke="#6366f1" strokeWidth="2" />
                <path d="M 0 0 L 0 -50 A 50 50 0 0 1 35 -35 Z" fill="url(#blueGradient)" />
                <path d="M 0 0 L 35 -35 A 50 50 0 0 1 50 0 Z" fill="url(#yellowGradient)" />
                <path d="M 0 0 L 50 0 A 50 50 0 0 1 0 50 Z" fill="#6366f1" opacity="0.5" />
            </g>

            {/* Gear Icons */}
            <g transform="translate(120, 520)">
                <circle cx="0" cy="0" r="20" fill="url(#blueGradient)" />
                <circle cx="0" cy="0" r="10" fill="#1e293b" />
                <rect x="-3" y="-25" width="6" height="10" fill="url(#blueGradient)" rx="2" />
                <rect x="-3" y="15" width="6" height="10" fill="url(#blueGradient)" rx="2" />
                <rect x="-25" y="-3" width="10" height="6" fill="url(#blueGradient)" rx="2" />
                <rect x="15" y="-3" width="10" height="6" fill="url(#blueGradient)" rx="2" />
            </g>

            <g transform="translate(680, 520)">
                <circle cx="0" cy="0" r="20" fill="#6366f1" opacity="0.7" />
                <circle cx="0" cy="0" r="10" fill="#1e293b" />
                <rect x="-3" y="-25" width="6" height="10" fill="#6366f1" rx="2" />
                <rect x="-3" y="15" width="6" height="10" fill="#6366f1" rx="2" />
                <rect x="-25" y="-3" width="10" height="6" fill="#6366f1" rx="2" />
                <rect x="15" y="-3" width="10" height="6" fill="#6366f1" rx="2" />
            </g>

            {/* Cylinder Database */}
            <g transform="translate(680, 450)">
                <ellipse cx="0" cy="0" rx="30" ry="10" fill="url(#blueGradient)" />
                <rect x="-30" y="0" width="60" height="40" fill="#4f46e5" />
                <ellipse cx="0" cy="40" rx="30" ry="10" fill="#6366f1" />
                <ellipse cx="0" cy="15" rx="30" ry="10" fill="#5b21b6" opacity="0.3" />
            </g>

            {/* Floating Percentage Labels */}
            <g transform="translate(250, 100)">
                <text fill="#6366f1" fontSize="16" fontWeight="bold" opacity="0.6">21%</text>
            </g>
            <g transform="translate(450, 420)">
                <text fill="#fbbf24" fontSize="16" fontWeight="bold" opacity="0.6">78%</text>
            </g>
            <g transform="translate(600, 380)">
                <text fill="#6366f1" fontSize="16" fontWeight="bold" opacity="0.6">67%</text>
            </g>

            {/* Mobile Device */}
            <g transform="translate(50, 300)">
                <rect x="0" y="0" width="60" height="100" fill="#1e293b" rx="8" stroke="#6366f1" strokeWidth="2" />
                <rect x="5" y="10" width="50" height="70" fill="url(#blueGradient)" rx="3" />
                <circle cx="30" cy="90" r="5" fill="#6366f1" />
            </g>

            {/* Animated Dots */}
            <circle cx="300" cy="500" r="3" fill="#fbbf24" opacity="0.5">
                <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" />
            </circle>
            <circle cx="500" cy="480" r="3" fill="#6366f1" opacity="0.5">
                <animate attributeName="opacity" values="0.5;1;0.5" dur="2.5s" repeatCount="indefinite" />
            </circle>
            <circle cx="400" cy="520" r="3" fill="#fbbf24" opacity="0.5">
                <animate attributeName="opacity" values="0.5;1;0.5" dur="3s" repeatCount="indefinite" />
            </circle>
        </svg>
    );
};

export default DataAnalyticsIllustration;
