import React from 'react';
import { Navbar, Nav, Container, NavDropdown, Badge } from 'react-bootstrap';
import { BsFillCartFill } from 'react-icons/bs';
import { Link } from 'react-router-dom';
import '../styles/CustomNavbar.css'; // Custom CSS for further styling

const CustomNavbar = ({ user, handleLogout, cart }) => {
  return (
    <Navbar expand="lg" fixed="top" className="custom-navbar">
      <Container>
        <Navbar.Brand as={Link} to="/" className="brand-logo">
          Book Bazaar
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto align-items-center">
            {/* You can add a search bar here if needed */}
            {user ? (
              <>
                <Nav.Link as={Link} to="/profile">{user.username}</Nav.Link>
                <Nav.Link onClick={handleLogout}>Logout</Nav.Link>
              </>
            ) : (
              <NavDropdown title="Login / Register" id="login-register-dropdown">
                <NavDropdown.Item as={Link} to="/login">Login</NavDropdown.Item>
                <NavDropdown.Item as={Link} to="/register">Register</NavDropdown.Item>
              </NavDropdown>
            )}
            <Nav.Link as={Link} to="/cart" className="position-relative">
              <BsFillCartFill size={20} />
              <Badge pill bg="secondary" className="cart-badge">
                {cart.length}
              </Badge>
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default CustomNavbar;
