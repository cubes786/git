// CustomNavbar.js
import React, { useState } from 'react';
import { Navbar, Nav, Container, Dropdown, Badge, Form, FormControl } from 'react-bootstrap';
import {
  BsSearch,
  BsPerson,
  BsBoxArrowInRight, 
  BsPencilSquare,    
} from 'react-icons/bs';
import { BsCartFill, BsCart } from 'react-icons/bs';
import { Link } from 'react-router-dom';
import CustomToggle from './CustomToggle'; // Ensure this is the correct path
import { useNavigate } from 'react-router-dom';
import '../styles/CustomNavbar.css';


const CustomNavbar = ({ user, handleLogout, cart, onSearch }) => {
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);
  };

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    onSearch(searchQuery);
  };

  const onLogout = () => {
    handleLogout();
    navigate('/');
  };

  return (
    <Navbar expand="lg" fixed="top" className="custom-navbar">
      <Container>
        <Navbar.Brand as={Link} to="/" className="brand-logo">
          Book Bazaar
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />

        <Navbar.Collapse id="basic-navbar-nav">
          <Form onSubmit={handleSearchSubmit} className="d-flex mx-auto search-form">
            <FormControl
              type="search"
              placeholder="Search books..."
              className="search-input"
              aria-label="Search"
              value={searchQuery}
              onChange={handleSearchChange}
            />
            <button type="submit" className="search-button">
              <BsSearch />
            </button>
          </Form>

          <Nav className="ms-auto align-items-center">
            {user ? (
              <>
                <Nav.Link as={Link} to="/profile">{user.username}</Nav.Link>
                <Nav.Link onClick={onLogout}>Logout</Nav.Link>
              </>
            ) : (
              <Dropdown>
                <Dropdown.Toggle as={CustomToggle}>
                  <BsPerson className="profile-icon-spanning" size={30} />
                  <div className="dropdown-title-wrapper">
                    <div className="welcome-line">Welcome</div>
                    <div className="register-line">
                      Sign in / Register
                      <span className="dropdown-arrow"></span>
                    </div>
                  </div>
                </Dropdown.Toggle>

                <Dropdown.Menu className="auth-dropdown-menu">
                  <Dropdown.Item as={Link} to="/login">
                    <BsBoxArrowInRight /> {/* Login Icon */}
                    Login
                  </Dropdown.Item>
                  <Dropdown.Item as={Link} to="/register">
                    <BsPencilSquare /> {/* Register Icon */}
                    Register
                  </Dropdown.Item>
                </Dropdown.Menu>
              </Dropdown>
            )}
           <Nav.Link as={Link} to="/cart" className="cart-link d-flex align-items-center position-relative">
              <div className="cart-icon-wrapper position-relative">
                {cart.length > 0 ? (
                  <BsCartFill size={24} />
                ) : (
                  <BsCart size={24} />
                )}
                {cart.length > 0 && (
                  <Badge pill bg="secondary" className="cart-badge">
                    {cart.length}
                  </Badge>
                )}
              </div>
              <span className="cart-text ms-1">Cart</span>
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default CustomNavbar;
