import React, { useState } from "react";
import api from "../api";
import "../App.css";
import "./Editor.css";

export default function CodeEditor() {
  const [code, setCode] = useState(`# Write your Python code here\nprint("Hello PyPath")`);
  const [output, setOutput] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleRun = async () => {
    setLoading(true);
    setOutput("");
    setError("");

    try {
      const res = await api.post("/editor/execute", { code });
      setOutput(res.data.output || "");
      setError(res.data.error || "");
    } catch (err) {
      setError(err.response?.data?.detail || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>Python Editor</h1>

      <div className="editor-container">
        <div className="editor-section card">
          <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
          />
          <button onClick={handleRun} disabled={loading}>
            {loading ? "Running..." : "Run Code"}
          </button>
        </div>

        <div className="console-section card">
          <h3>Output:</h3>
          <pre>{output}</pre>
          {error && (
            <>
              <h3 style={{ color: "#f87171" }}>Error:</h3>
              <pre style={{ color: "#f87171" }}>{error}</pre>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
