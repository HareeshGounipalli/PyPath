import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import "./Navbar.css";

function Navbar({ isAuthenticated, setIsAuthenticated }) {
  const navigate = useNavigate();
  const [showLogoutConfirm, setShowLogoutConfirm] = useState(false);

  const handleLogout = () => {
    localStorage.removeItem("token");
    setIsAuthenticated(false);
    navigate("/login");
  };

  return (
    <nav className="navbar">
      {/* Left Section: Home + Tutorials */}
      <div className="nav-left">
        <Link to="/">Home</Link>
        <Link to="/tutorials">Tutorials</Link>
      </div>

      {/* Middle Section: Editor (only for logged-in users) */}
      {isAuthenticated && (
        <div className="nav-center">
          <Link to="/editor">Editor</Link>
        </div>
      )}

      {/* Right Section: Login / Logout */}
      <div className="nav-right">
        {isAuthenticated ? (
          <>
            <button className="logout-button" onClick={() => setShowLogoutConfirm(true)}>
              Logout
            </button>

            {showLogoutConfirm && (
              <div className="dialog-overlay">
                <div className="dialog">
                  <p>Are you sure you want to logout?</p>
                  <div className="dialog-buttons">
                    <button className="confirm-button" onClick={handleLogout}>Yes</button>
                    <button className="cancel-button" onClick={() => setShowLogoutConfirm(false)}>No</button>
                  </div>
                </div>
              </div>
            )}
          </>
        ) : (
          <Link to="/auth">Login</Link>
        )}
      </div>
    </nav>
  );
}

export default Navbar;

