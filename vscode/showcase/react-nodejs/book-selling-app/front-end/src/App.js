import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import BookList from './components/BookList';
import BookDetails from './components/BookDetails';
import UserRegistration from './components/UserRegistration';
import UserLogin from './components/UserLogin';
import ShoppingCart from './components/ShoppingCart';
import CheckoutForm from './components/CheckoutForm';
import UserProfile from './components/UserProfile';
import { Container, Navbar, Nav, NavDropdown, Badge } from 'react-bootstrap';
import { BsFillCartFill } from "react-icons/bs";
import { useCart } from './contexts/CartContext';

function App() {
    const [user, setUser] = useState(null);
    const { cart, clearCart } = useCart();

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

    return (
        <Router>
            <Navbar bg="dark" variant="dark" className="p-3" fixed="top">
                <Container>
                    <Navbar.Brand as={Link} to="/">Book Selling App</Navbar.Brand>
                    <Nav className="ms-auto">
                        {user ? (
                            <>
                                <Nav.Link as={Link} to="/profile">{user.username}</Nav.Link>
                                <Nav.Link as={Link} to="/" onClick={handleLogout}>Logout</Nav.Link>
                            </>
                        ) : (
                            <NavDropdown title="Login / Register" id="login-register-dropdown">
                                <NavDropdown.Item as={Link} to="/login">Login</NavDropdown.Item>
                                <NavDropdown.Item as={Link} to="/register">Register</NavDropdown.Item>
                            </NavDropdown>
                        )}
                        <Nav.Link as={Link} to="/cart" className="position-relative">
                            <BsFillCartFill style={{ marginBottom: '5px', marginRight: '5px' }} />
                            <Badge pill bg="secondary" style={{ position: "absolute", top: "1px" }}>
                                {cart.length}
                            </Badge>
                        </Nav.Link>
                    </Nav>
                </Container>
            </Navbar>

            <Container style={{ marginTop: "80px" }}>
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
