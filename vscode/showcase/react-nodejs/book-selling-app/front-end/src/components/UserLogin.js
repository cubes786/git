// frontend/src/components/UserLogin.js
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const UserLogin = ({ setUser }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();

        // Check if a user is already logged in
        const existingUser = sessionStorage.getItem('user');
        if (existingUser) {
            setMessage('You are already logged in. Please log out first.');
            return;
        }

        try {
            // Send login request to the backend
            const response = await axios.post('http://localhost:3001/users/login', {
                username,
                password,
            });

            // Store user information and JWT in sessionStorage
            const loggedInUser = response.data.user;
            const accessToken = response.data.accessToken;
            sessionStorage.setItem('user', JSON.stringify(loggedInUser));
            sessionStorage.setItem('token', accessToken);

            // Update global user state via setUser
            setUser(loggedInUser);

            // Redirect to home page
            navigate('/');
        } catch (error) {
            // Handle error and display message
            setMessage(error.response?.data || 'Login failed. Please try again.');
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Username:</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Login</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default UserLogin;