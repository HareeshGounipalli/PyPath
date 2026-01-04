import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../api";

export default function TutorialDetail() {
  const { id } = useParams();
  const [tutorial, setTutorial] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let isMounted = true;
    setLoading(true);
    api.get(`/tutorials/${id}`)
      .then((res) => {
        if (isMounted) setTutorial(res.data);
      })
      .catch((err) => console.error(err))
      .finally(() => {
        if (isMounted) setLoading(false);
      });

    return () => { isMounted = false; };
  }, [id]);

  if (loading) return <div className="card">Loading tutorial...</div>;
  if (!tutorial) return <div className="card">Tutorial not found</div>;

  return (
    <div>
      <h1>{tutorial.title}</h1>
      <div className="card">{tutorial.description || "No description available"}</div>

      <h2>Lessons</h2>
      {tutorial.lessons && tutorial.lessons.length > 0 ? (
        <ul>
          {tutorial.lessons.map((lesson) => (
            <li key={lesson.id} className="card">
              <strong>{lesson.title}</strong>
              <p>{lesson.content}</p>
            </li>
          ))}
        </ul>
      ) : (
        <div className="card">No lessons available</div>
      )}

      <Link to="/tutorials" className="card" style={{ display: "inline-block", marginTop: "1rem" }}>
        Back to Tutorials
      </Link>
    </div>
  );
}
