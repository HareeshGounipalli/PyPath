import { Link, useNavigate } from "react-router-dom";

export default function Navbar() {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/auth?mode=login");
  };

  return (
    <nav className="navbar">
      <Link to="/">Home</Link>
      <Link to="/tutorials">Tutorials</Link>

      {!token ? (
        <Link to="/auth?mode=login">Login</Link>
      ) : (
        <button onClick={logout}>Logout</button>
      )}
    </nav>
  );
}
