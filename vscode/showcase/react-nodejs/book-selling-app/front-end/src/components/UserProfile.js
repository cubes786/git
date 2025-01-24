// frontend/src/components/UserProfile.js
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


const UserProfile = () => {
   const navigate = useNavigate();
   const [orders, setOrders] = useState([]);
   const [user,setUser] = useState(null);

  useEffect(()=>{
       const storedUser = sessionStorage.getItem('user');
       if(storedUser){
          setUser(JSON.parse(storedUser));
       }
    const fetchOrders = async () => {
        try {
           const response = await axios.get('http://localhost:3001/orders');
           setOrders(response.data);
        } catch (error) {
          console.error('Error fetching order', error);
         }
       }
     fetchOrders();
  },[]);

  if(!user){
       return <p>Not logged in</p>
   }

   const handleLogout = ()=>{
       sessionStorage.removeItem('user');
       navigate('/');
   }
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
             {orders.map(order=>(
                 <li key={order.id}>Order Id: {order.id} -- Order Status: {order.orderStatus}</li>
             ))}
            </ul>
        </div>
   )
};

export default UserProfile;