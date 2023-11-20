import './App.css';
import logo from './logo.svg';
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import LoginForm from './components/LoginForm';
import ProfilePage from './components/ProfilePage';

function App() {
  const [user, setUser] = useState(null);

  const handleLogin = (username, password) => {
    // Replace this with your actual login logic
    setUser({ username, password });
  };

  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={user ? <Navigate to="/profile" /> : <LoginForm onLogin={handleLogin} />} />
        <Route path="/profile" element={!user ? <Navigate to="/login" /> : <ProfilePage user={user} />} />
      </Routes>
    </Router>
  );
}

function HomePage() {
  return (
    <div>
      <header className="App-header">
         <img src={logo} className="App-logo" alt="logo" />
         <a
           className="App-link"
           href="https://reactjs.org"
           target="_blank"
           rel="noopener noreferrer"
         >
           Learn React
         </a>
       </header>
      <h1>Welcome to My App</h1>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '50vh' }}>
        <p><a className="App-link" href="/login">Login</a></p>  
        <p><a className="App-link" href="/profile">Go to Profile</a></p>
      </div>
    </div>
  );
}


export default App;
