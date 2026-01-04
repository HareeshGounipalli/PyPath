import React, { useRef } from "react";
import { Routes, Route, Link, useLocation } from "react-router-dom";
import { CSSTransition, TransitionGroup } from "react-transition-group";

import Home from "./pages/Home";
import Tutorials from "./pages/Tutorials";
import TutorialDetail from "./pages/TutorialDetail";
import Login from "./pages/Login";
import ProtectedRoute from "./components/ProtectedRoute";
import Auth from "./pages/Auth";

export default function App() {
  const location = useLocation();
  const nodeRef = useRef(null); // Needed for React 18 CSSTransition

  return (
    <div className="app-container">
      <nav>
        <Link to="/">Home</Link>
        <Link to="/tutorials">Tutorials</Link>
         <Link to="/login">Login</Link>
      </nav>

      <TransitionGroup className="transition-group">
        <CSSTransition
          key={location.pathname}
          timeout={400}
          classNames="page"
          nodeRef={nodeRef}
          unmountOnExit
        >
          <div ref={nodeRef}>
            <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />

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
        <Route path="/auth" element={<Auth />} />

      </Routes>
          </div>
        </CSSTransition>
      </TransitionGroup>
    </div>
  );
}
