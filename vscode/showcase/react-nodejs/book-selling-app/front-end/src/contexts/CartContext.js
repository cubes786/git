import React, { createContext, useState, useContext } from 'react';

const CartContext = createContext();

export const CartProvider = ({ children }) => {
    const [cart, setCart] = useState([]);
    const [warningMessage, setWarningMessage] = useState(''); // Warning message for unauthorized actions

    const addToCart = (book) => {
        const user = sessionStorage.getItem('user');
        if (!user) {
            setWarningMessage('You need to log in to add items to the cart.'); // Warning for guests
            return;
        }

        // Clear any existing warnings if the user is logged in
        setWarningMessage('');

        setCart((prevCart) => {
            const existingItem = prevCart.find((item) => item.id === book.id);
            if (existingItem) {
                return prevCart.map((item) =>
                    item.id === book.id ? { ...item, quantity: item.quantity + 1 } : item
                );
            } else {
                return [...prevCart, { ...book, quantity: 1 }];
            }
        });
    };

    const removeFromCart = (bookId) => {
        setCart((prevCart) => prevCart.filter((item) => item.id !== bookId));
    };

    const updateQuantity = (bookId, quantity) => {
        setCart((prevCart) =>
            prevCart.map((item) =>
                item.id === bookId ? { ...item, quantity: parseInt(quantity, 10) } : item
            )
        );
    };

    const clearCart = () => {
        setCart([]);
    };

    return (
        <CartContext.Provider
            value={{
                cart,
                addToCart,
                removeFromCart,
                updateQuantity,
                clearCart,
                warningMessage,
                setWarningMessage,
            }}
        >
            {children}
        </CartContext.Provider>
    );
};

export const useCart = () => {
    return useContext(CartContext);
};
