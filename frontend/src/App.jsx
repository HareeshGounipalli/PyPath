import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Tutorials from "./pages/Tutorials";
import TutorialDetail from "./pages/TutorialDetail";

export default function App() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link> | <Link to="/tutorials">Tutorials</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/tutorials" element={<Tutorials />} />
        <Route path="/tutorials/:id" element={<TutorialDetail />} />
      </Routes>
    </div>
  );
}
