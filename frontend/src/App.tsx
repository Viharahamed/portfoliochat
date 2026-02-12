import Header from './components/Header';
import Hero from './components/Hero';
import Experience from './components/Experience';
import Projects from './components/Projects';
import Skills from './components/Skills';
import Contact from './components/Contact';
import ChatWidget from './components/ChatWidget';
import './App.css';

function App() {
    return (
        <div className="App">
            <Header />
            <main>
                <Hero />
                <Experience />
                <Projects />
                <Skills />
                <Contact />
            </main>
            <ChatWidget />
        </div>
    );
}

export default App;
