import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';

function NavBar({ user, onLogout }) {
    function handleLogoutClick() {
      fetch("/logout", { method: "DELETE" }).then((r) => {
        if (r.ok) {
          onLogout(null);
        }
      });
    }
  
    if (user) {
      return (
        <Navbar bg="primary" data-bs-theme="dark">
          <Nav className="me-auto">
            <Nav.Link href="/home">Home</Nav.Link>
            <Nav.Link href="/logout" onClick={handleLogoutClick}>
              Logout
            </Nav.Link>
          </Nav>
        </Navbar>
      );
    } else {
      return (
        <Navbar bg="primary" data-bs-theme="dark">
          <Nav className="me-auto">
            <Nav.Link href="/signup">signup</Nav.Link>
            <Nav.Link href="/login">login</Nav.Link>
          </Nav>
        </Navbar>
      );
    }
  }
  
  export default NavBar;

