// frontend/src/components/CheckoutForm.js
import React from 'react';
import { useCart } from '../contexts/CartContext';
import axios from 'axios';
import {useNavigate} from 'react-router-dom';

  const CheckoutForm = () => {
  const { cart, clearCart} = useCart();
   const navigate = useNavigate();

 const handleSubmit = async () => {
    const user = JSON.parse(sessionStorage.getItem('user'));
    if(!user){
        return;
    }
      try {
            const response = await axios.post('http://localhost:3001/orders', {
                userId: user.id,
               orderItems: cart
            });
            console.log(response.data);
            clearCart();
            navigate('/');
        } catch (error) {
            console.error('Error placing order',error);
        }
    };

     if(cart.length === 0) {
            return <p>You need to add books before checking out</p>
        }

    return (
    <div>
        <h2>Checkout</h2>
        <button onClick={handleSubmit}>Place Order</button>
     </div>
     );
  };

  export default CheckoutForm;