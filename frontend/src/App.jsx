import React, { useRef } from "react";
import { Routes, Route, Link, useLocation } from "react-router-dom";
import { CSSTransition, TransitionGroup } from "react-transition-group";

import Home from "./pages/Home";
import Tutorials from "./pages/Tutorials";
import TutorialDetail from "./pages/TutorialDetail";

export default function App() {
  const location = useLocation();
  const nodeRef = useRef(null); // Needed for React 18 CSSTransition

  return (
    <div className="app-container">
      <nav>
        <Link to="/">Home</Link>
        <Link to="/tutorials">Tutorials</Link>
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
            <Routes location={location}>
              <Route path="/" element={<Home />} />
              <Route path="/tutorials" element={<Tutorials />} />
              <Route path="/tutorials/:id" element={<TutorialDetail />} />
            </Routes>
          </div>
        </CSSTransition>
      </TransitionGroup>
    </div>
  );
}
