import React from 'react';
import { useCart } from '../contexts/CartContext';
import { Link, useNavigate } from 'react-router-dom';
import { BsFillTrashFill } from 'react-icons/bs';

const ShoppingCart = () => {
    const { cart, removeFromCart, updateQuantity, warningMessage, setWarningMessage } = useCart();
    const navigate = useNavigate();

    const handleQuantityChange = (bookId, quantity) => {
        const user = sessionStorage.getItem('user');
        if (!user) {
            setWarningMessage('You need to log in to update the quantity in the cart.');
            return;
        }
        updateQuantity(bookId, quantity);
        setWarningMessage(''); // Clear warning after successful action
    };

    const handleRemoveFromCart = (bookId) => {
        const user = sessionStorage.getItem('user');
        if (!user) {
            setWarningMessage('You need to log in to remove items from the cart.');
            return;
        }
        removeFromCart(bookId);
        setWarningMessage(''); // Clear warning after successful action
    };

    const calculateTotal = () => {
        return cart.reduce((total, item) => total + item.price * item.quantity, 0);
    };

    const user = sessionStorage.getItem('user');

    if (cart.length === 0) {
        return (
            <div>
                <p>Your cart is empty.</p>
                {!user && (
                    <p style={{ color: 'red' }}>
                        You need to log in to add items to your cart.{' '}
                        <button onClick={() => navigate('/login')}>Log in</button>
                    </p>
                )}
                <Link to="/">Go back to the list of books.</Link>
            </div>
        );
    }

    return (
        <div>
            <h2>Shopping Cart</h2>
            <ul>
                {cart.map((item) => (
                    <li key={item.id}>
                        <h3>{item.title}</h3>
                        <p>Price: ${item.price}</p>
                        <input
                            type="number"
                            value={item.quantity}
                            min="1"
                            onChange={(e) => handleQuantityChange(item.id, e.target.value)}
                        />
                        <button onClick={() => handleRemoveFromCart(item.id)}>
                            <BsFillTrashFill />
                        </button>
                    </li>
                ))}
            </ul>
            <p>Total: ${calculateTotal().toFixed(2)}</p>
            <Link to="/checkout">Proceed to checkout</Link>

            {/* Display Warning Message */}
            {warningMessage && (
                <div style={{ color: 'red', marginTop: '20px' }}>
                    <p>{warningMessage}</p>
                    <button
                        onClick={() => {
                            setWarningMessage('');
                            navigate('/login'); // Redirect to login page
                        }}
                    >
                        Log in to continue
                    </button>
                </div>
            )}
        </div>
    );
};

export default ShoppingCart;
