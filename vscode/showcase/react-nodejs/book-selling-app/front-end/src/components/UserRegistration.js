// frontend/src/components/UserRegistration.js
import React, { useState } from 'react';
import axios from 'axios';
import {useNavigate} from 'react-router-dom';

  const UserRegistration = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
      const [address, setAddress] = useState('');
      const [contactDetails, setContactDetails] = useState('');
    const [message, setMessage] = useState('');
     const navigate = useNavigate();

    const handleSubmit = async (event) => {
      event.preventDefault();
      try {
        const response = await axios.post('http://localhost:3001/users/register', {
          username,
          password,
            address,
            contactDetails
        });
        setMessage(response.data);
           navigate('/login');
      } catch (error) {
        setMessage(error.response.data);
      }
    };

    return (
      <div>
        <h2>Register</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label>Username:</label>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
          </div>
          <div>
            <label>Password:</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </div>
           <div>
            <label>Address:</label>
            <input type="text" value={address} onChange={(e) => setAddress(e.target.value)} />
          </div>
           <div>
            <label>Contact Details:</label>
            <input type="text" value={contactDetails} onChange={(e) => setContactDetails(e.target.value)} />
          </div>
          <button type="submit">Register</button>
        </form>
        {message && <p>{message}</p>}
      </div>
    );
  };

  export default UserRegistration;