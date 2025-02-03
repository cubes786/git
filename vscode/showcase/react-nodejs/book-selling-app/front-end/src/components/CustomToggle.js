// CustomToggle.js
import React from 'react';
import { Dropdown } from 'react-bootstrap';

const CustomToggle = React.forwardRef(({ children, onClick }, ref) => (
  <a
    href="#"
    ref={ref}
    onClick={(e) => {
      e.preventDefault();
      onClick(e);
    }}
    className="nav-link d-flex align-items-center position-relative"
    id="login-register-dropdown"
  >
    {children}
  </a>
));

export default CustomToggle;
