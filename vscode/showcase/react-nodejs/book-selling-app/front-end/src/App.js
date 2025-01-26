import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import BookList from './components/BookList';
import BookDetails from './components/BookDetails';
import UserRegistration from './components/UserRegistration';
import UserLogin from './components/UserLogin';
import ShoppingCart from './components/ShoppingCart';
import CheckoutForm from './components/CheckoutForm';
import UserProfile from './components/UserProfile';
import { Container, Navbar, Nav, Badge } from 'react-bootstrap';
import { BsFillCartFill } from "react-icons/bs";
import { useCart } from './contexts/CartContext';

function App() {
    const [user, setUser] = useState(null);
    const { cart, clearCart } = useCart();

    // Retrieve the user from sessionStorage on component mount
    useEffect(() => {
        const storedUser = sessionStorage.getItem('user');
        if (storedUser) {
            setUser(JSON.parse(storedUser));
        }
    }, []);

    // Save cart to sessionStorage whenever it changes
    useEffect(() => {
        sessionStorage.setItem("cart", JSON.stringify(cart));
    }, [cart]);

    const handleLogout = () => {
        sessionStorage.removeItem('user'); // Clear user from sessionStorage
        clearCart(); // Clear the cart
        setUser(null); // Reset user state
    };

    return (
        <Router>
            {/* Navbar Section */}
            <Navbar bg="dark" variant="dark" className="p-3" fixed="top">
                <Container>
                    <Navbar.Brand as={Link} to="/">Book Selling App</Navbar.Brand>
                    <Nav className="ms-auto">
                        <Nav.Link as={Link} to="/">Home</Nav.Link>
                        <Nav.Link as={Link} to="/cart" className="position-relative">
                            <BsFillCartFill style={{ marginBottom: '5px', marginRight: '5px' }} />
                            <Badge pill bg="secondary" style={{ position: "absolute", top: "1px" }}>
                                {cart.length}
                            </Badge>
                        </Nav.Link>
                        {user ? (
                            <>
                                <Nav.Link as={Link} to="/profile">{user.username}</Nav.Link>
                                <Nav.Link as={Link} to="/" onClick={handleLogout}>Logout</Nav.Link>
                            </>
                        ) : (
                            <>
                                <Nav.Link as={Link} to="/register">Register</Nav.Link>
                                <Nav.Link as={Link} to="/login">Login</Nav.Link>
                            </>
                        )}
                    </Nav>
                </Container>
            </Navbar>

            {/* Routes */}
            <Container style={{ marginTop: "80px" }}> {/* Add margin to avoid overlap with fixed navbar */}
                <Routes>
                    <Route path="/" element={<BookList />} />
                    <Route path="/books/:bookId" element={<BookDetails />} />
                    <Route path="/register" element={<UserRegistration />} />
                    <Route path="/login" element={<UserLogin setUser={setUser} />} />
                    <Route path="/cart" element={<ShoppingCart />} />
                    <Route path="/checkout" element={<CheckoutForm />} />
                    <Route path="/profile" element={<UserProfile setUser={setUser} />} />
                </Routes>
            </Container>
        </Router>
    );
}

export default App;
