import React, { useState, useRef, useEffect } from 'react';
import type { ChatMessage } from '../types';
import { apiService } from '../services/api';
import './ChatWidget.css';

const ChatWidget: React.FC = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState<ChatMessage[]>([]);
    const [inputValue, setInputValue] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [sessionId, setSessionId] = useState<string | undefined>();
    const messagesEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSendMessage = async () => {
        if (!inputValue.trim() || isLoading) return;

        const userMessage: ChatMessage = {
            role: 'user',
            content: inputValue,
        };

        setMessages((prev) => [...prev, userMessage]);
        setInputValue('');
        setIsLoading(true);

        try {
            const response = await apiService.sendChatMessage(inputValue, sessionId);

            if (!sessionId) {
                setSessionId(response.session_id);
            }

            const aiMessage: ChatMessage = {
                role: 'assistant',
                content: response.response,
            };

            setMessages((prev) => [...prev, aiMessage]);
        } catch (error) {
            console.error('Chat error:', error);
            let errorMessageContent = 'Sorry, I encountered an error. Please try again.';

            if (error instanceof Error) {
                if (error.message.includes('504') || error.message.includes('timeout')) {
                    errorMessageContent = 'The AI service is taking longer than expected. Please try again later.';
                } else if (error.message.includes('500')) {
                    errorMessageContent = 'I am having trouble connecting to the AI service. Please try again later.';
                }
            }

            const errorMessage: ChatMessage = {
                role: 'assistant',
                content: errorMessageContent,
            };
            setMessages((prev) => [...prev, errorMessage]);
        } finally {
            setIsLoading(false);
        }
    };

    const handleKeyPress = (e: React.KeyboardEvent) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    };

    return (
        <div className="chat-widget">
            {!isOpen && (
                <button className="chat-toggle" onClick={() => setIsOpen(true)}>
                    <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                    </svg>
                    <span className="chat-badge">AI</span>
                </button>
            )}

            {isOpen && (
                <div className="chat-container glass">
                    <div className="chat-header">
                        <div className="chat-header-content">
                            <div className="chat-avatar">
                                <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z" />
                                </svg>
                            </div>
                            <div>
                                <h3>AI Assistant</h3>
                                <p>Ask me anything about this portfolio!</p>
                            </div>
                        </div>
                        <button className="chat-close" onClick={() => setIsOpen(false)}>
                            <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    </div>

                    <div className="chat-messages">
                        {messages.length === 0 && (
                            <div className="chat-welcome">
                                <p>👋 Hi! I'm an AI assistant trained on this portfolio.</p>
                                <p>Ask me about:</p>
                                <ul>
                                    <li>Work experience</li>
                                    <li>Technical skills</li>
                                    <li>Projects</li>
                                    <li>Education</li>
                                </ul>
                            </div>
                        )}
                        {messages.map((message, index) => (
                            <div key={index} className={`message ${message.role}`}>
                                <div className="message-content">
                                    {message.content}
                                </div>
                            </div>
                        ))}
                        {isLoading && (
                            <div className="message assistant">
                                <div className="message-content typing">
                                    <span></span>
                                    <span></span>
                                    <span></span>
                                </div>
                            </div>
                        )}
                        <div ref={messagesEndRef} />
                    </div>

                    <div className="chat-input-container">
                        <input
                            type="text"
                            className="chat-input"
                            placeholder="Ask me anything..."
                            value={inputValue}
                            onChange={(e) => setInputValue(e.target.value)}
                            onKeyPress={handleKeyPress}
                            disabled={isLoading}
                        />
                        <button
                            className="chat-send"
                            onClick={handleSendMessage}
                            disabled={!inputValue.trim() || isLoading}
                        >
                            <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                            </svg>
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default ChatWidget;
