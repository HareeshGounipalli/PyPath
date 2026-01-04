import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import './Navbar.css';

export default function Navbar({ isAuthenticated, setIsAuthenticated }) {
  const navigate = useNavigate();
  const [showLogoutConfirm, setShowLogoutConfirm] = useState(false);

  const handleLogout = () => {
    // Remove token & update state
    localStorage.removeItem("token");
    setIsAuthenticated(false);
    setShowLogoutConfirm(false);
    navigate("/login");
  };

  return (
    <nav className="navbar">
      <Link to="/">Home</Link>
      <Link to="/tutorials">Tutorials</Link>

      {isAuthenticated ? (
        <>
          <button
            className="logout-button"
            onClick={() => setShowLogoutConfirm(true)}
          >
            Logout
          </button>

          {showLogoutConfirm && (
            <div className="logout-dialog-overlay">
              <div className="logout-dialog">
                <p>Are you sure you want to logout?</p>
                <div className="logout-dialog-buttons">
                  <button
                    className="confirm-button"
                    onClick={handleLogout}
                  >
                    Yes
                  </button>
                  <button
                    className="cancel-button"
                    onClick={() => setShowLogoutConfirm(false)}
                  >
                    No
                  </button>
                </div>
              </div>
            </div>
          )}
        </>
      ) : (
        <Link to="/login" className="login-link">Login</Link>
      )}
    </nav>
  );
}
