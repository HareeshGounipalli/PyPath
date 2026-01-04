import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../api";

export default function TutorialDetail() {
  const { id } = useParams();

  const [tutorial, setTutorial] = useState(null);
  const [completedLessons, setCompletedLessons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!id) return;

    Promise.all([
      api.get(`/tutorials/${id}`),
      api.get(`/tutorials/${id}/progress`).catch(() => ({ data: { completedLessons: [] } }))
    ])
      .then(([tutorialRes, progressRes]) => {
        setTutorial(tutorialRes.data);
        setCompletedLessons(progressRes.data.completedLessons || []);
      })
      .catch((err) => {
        console.error(err);
        setError("Failed to load tutorial");
      })
      .finally(() => setLoading(false));
  }, [id]);

  /* ---------------- UI STATES ---------------- */

  if (loading) {
    return <div className="card">Loading tutorial...</div>;
  }

  if (error) {
    return <div className="card">{error}</div>;
  }

  if (!tutorial) {
    return <div className="card">Tutorial not found</div>;
  }

  /* ---------------- MAIN UI ---------------- */

  return (
    <div>
      <h1>{tutorial.title}</h1>
      <p>{tutorial.description}</p>

      <h2>Lessons</h2>

      {tutorial.lessons && tutorial.lessons.length > 0 ? (
        <ul>
          {tutorial.lessons.map((lesson) => (
            <li key={lesson.id} className="card">
              <strong>{lesson.title}</strong>
              {completedLessons.includes(lesson.id) && (
                <span style={{ color: "#61dafb", marginLeft: "0.5rem" }}>
                  ✓ Completed
                </span>
              )}
            </li>
          ))}
        </ul>
      ) : (
        <div className="card">No lessons available</div>
      )}

      <Link
        to="/tutorials"
        className="card"
        style={{ marginTop: "1rem", display: "inline-block" }}
      >
        ← Back to Tutorials
      </Link>
    </div>
  );
}
