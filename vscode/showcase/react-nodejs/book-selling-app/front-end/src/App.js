import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import BookList from './components/BookList';
import BookDetails from './components/BookDetails';
import UserRegistration from './components/UserRegistration';
import UserLogin from './components/UserLogin';
import ShoppingCart from './components/ShoppingCart';
import CheckoutForm from './components/CheckoutForm';
import UserProfile from './components/UserProfile';
import CustomNavbar from './components/CustomNavbar';
import { Container } from 'react-bootstrap';
import { useCart } from './contexts/CartContext';
import './App.css';

function App() {
    const [user, setUser] = useState(null);
    const { cart, clearCart } = useCart();
    const [searchQuery, setSearchQuery] = useState('');

    useEffect(() => {
        const storedUser = sessionStorage.getItem('user');
        if (storedUser) {
            setUser(JSON.parse(storedUser));
        }
    }, []);

    useEffect(() => {
        sessionStorage.setItem("cart", JSON.stringify(cart));
    }, [cart]);

    const handleLogout = () => {
        sessionStorage.removeItem('user');
        clearCart();
        setUser(null);
    };

    const handleSearch = (query) => {
        setSearchQuery(query);
    };

    return (
        <Router>
            <CustomNavbar user={user} handleLogout={handleLogout} cart={cart} onSearch={handleSearch} />
            <Container style={{ marginTop: "90px" }}>
                <Routes>
                    <Route path="/" element={<BookList searchQuery={searchQuery} />} />
                    <Route path="/books/:bookId" element={<BookDetails />} />
                    <Route path="/register" element={<UserRegistration />} />
                    <Route path="/login" element={<UserLogin setUser={setUser} />} />
                    <Route path="/cart" element={<ShoppingCart />} />
                    <Route path="/checkout" element={<CheckoutForm />} />
                    <Route path="/profile" element={<UserProfile user={user} setUser={setUser} />} />
                </Routes>
            </Container>
        </Router>
    );
}

export default App;