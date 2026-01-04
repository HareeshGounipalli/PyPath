import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import ProtectedRoute from  "./components/ProtectedRoute";
import Home from "./pages/Home";
import Tutorials from  "./pages/Tutorials";
import TutorialDetail from  "./pages/TutorialDetail";
import Auth from "./pages/Auth"; // login/register page
import './index.css';
import './App.css';

export default function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(
    !!localStorage.getItem("token")
  );
  
  return (
    <div className="app-container">
      <Navbar isAuthenticated={isAuthenticated} setIsAuthenticated={setIsAuthenticated} />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Auth setIsAuthenticated={setIsAuthenticated} />} />
        <Route path="/auth" element={<Auth  setIsAuthenticated={setIsAuthenticated} />} />

        <Route
          path="/tutorials"
          element={
            <ProtectedRoute>
              <Tutorials />
            </ProtectedRoute>
          }
        />

        <Route
          path="/tutorials/:id"
          element={
            <ProtectedRoute>
              <TutorialDetail />
            </ProtectedRoute>
          }
        />
      </Routes>
    </div>
  );
}
