import React, { useState, useEffect } from "react";
import api from "../api";
import "../App.css";
import "./Editor.css";
import FileTree from "./FileTree"; // file structure panel

export default function CodeEditor() {
  // Load files from localStorage or default
  const [files, setFiles] = useState(() => {
    const saved = localStorage.getItem("editor-files");
    if (saved) return JSON.parse(saved);
    return [{ id: 1, name: "main.py", content: 'print("Hello PyPath")' }];
  });

  const [activeFile, setActiveFile] = useState(() => {
    const saved = localStorage.getItem("editor-active-file");
    if (saved) return JSON.parse(saved);
    return files[0];
  });

  const [output, setOutput] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  // Persist files and active file
  useEffect(() => {
    localStorage.setItem("editor-files", JSON.stringify(files));
    localStorage.setItem("editor-active-file", JSON.stringify(activeFile));
  }, [files, activeFile]);

  const handleRun = async () => {
    if (!activeFile?.content) return;
    setLoading(true);
    setOutput("");
    setError("");

    try {
      const res = await api.post("/editor/execute", { code: activeFile.content });
      setOutput(res.data.output || "");
      setError(res.data.error || "");
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.detail || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  const handleCodeChange = (e) => {
    const updatedContent = e.target.value;
    setActiveFile({ ...activeFile, content: updatedContent });

    // Update in files array
    const updatedFiles = files.map(f => f.id === activeFile.id ? { ...f, content: updatedContent } : f);
    setFiles(updatedFiles);
  };

  return (
    <div className="app-container">
      <h1>Python Editor</h1>
      <div className="editor-wrapper">
        {/* FileTree Panel */}
        <FileTree
          files={files}
          setFiles={setFiles}
          activeFile={activeFile}
          setActiveFile={setActiveFile}
        />

        {/* Editor + Console */}
        <div className="editor-console">
          <div className="editor-card card">
            <textarea
              value={activeFile.content}
              onChange={handleCodeChange}
              className="editor-textarea"
            />
            <button
              className="run-button"
              onClick={handleRun}
              disabled={loading}
            >
              {loading ? "Running..." : "Run Code"}
            </button>
          </div>

          <div className="console-card card">
            <h3>Output:</h3>
            <pre className="console-output">{output}</pre>
            {error && (
              <>
                <h3 className="console-error">Error:</h3>
                <pre className="console-error">{error}</pre>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
