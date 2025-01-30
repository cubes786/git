// frontend/src/components/UserProfile.js
import React, {useState, useEffect} from 'react';
import axios from 'axios';

const UserProfile = ({ setUser }) => {
    const [orders, setOrders] = useState([]);
    const [user, setLocalUser] = useState(null);
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
    
    return (
        <div>
            <h2>User Profile</h2>
            <div>
                <p>Username : {user.username}</p>
                <p>Address: {user.address}</p>
                <p>Contact Details: {user.contactDetails}</p>                
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