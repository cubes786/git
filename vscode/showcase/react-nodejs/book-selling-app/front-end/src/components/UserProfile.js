// frontend/src/components/UserProfile.js
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { useCart } from '../contexts/CartContext';

const UserProfile = ({ setUser }) => {
    const navigate = useNavigate();
    const [orders, setOrders] = useState([]);
    const [user, setLocalUser] = useState(null);
    const { clearCart } = useCart();
    const token = sessionStorage.getItem('token');


    useEffect(() => {
          const fetchProfile = async () => {
            try {
                const response = await axios.get('http://localhost:3001/users/profile', {
                    headers: {
                        Authorization: 'Bearer ' + token,
                    },
                });
                  if(response.data.user) {
                      setUser(response.data.user);
                       setLocalUser(response.data.user);
                    }

            } catch (error) {
                console.error('Error fetching user profile', error);
            }
          };

         const fetchOrders = async () => {
            try {
                const response = await axios.get('http://localhost:3001/orders', {
                    headers: {
                        Authorization: 'Bearer ' + token,
                    },
                });
                setOrders(response.data);
            } catch (error) {
                console.error('Error fetching order', error);
            }
        };
        if(token) {
            fetchProfile();
            fetchOrders();
        }
   }, [token, setUser]);

    if (!user) {
        return <p>Not logged in</p>;
    }

    const handleLogout = () => {
        sessionStorage.removeItem('user');
        sessionStorage.removeItem('token');
         clearCart(); // Clear the cart
        setUser(null); // Reset user state in App.js
        setLocalUser(null); // Reset local user state
        navigate('/');
    };

    return (
        <div>
            <h2>User Profile</h2>
            <div>
                <p>Username : {user.username}</p>
                <p>Address: {user.address}</p>
                <p>Contact Details: {user.contactDetails}</p>
                <button onClick={handleLogout}>Logout</button>
            </div>
            <h2>Orders</h2>
            <ul>
                {orders.map((order) => (
                    <li key={order.id}>
                        Order Id: {order.id} -- Order Status: {order.orderStatus}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default UserProfile;