import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../api";

export default function Tutorials() {
  const [tutorials, setTutorials] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    let isMounted = true; // Prevent state update if unmounted
    api.get("/tutorials/")
      .then((res) => {
        if (isMounted) setTutorials(res.data);
      })
      .catch((err) => console.error(err))
      .finally(() => {
        if (isMounted) setLoading(false);
      });

    return () => { isMounted = false; }; // cleanup
  }, []);

  if (loading) return <div className="card">Loading tutorials...</div>;

  return (
    <div>
      <h1>Tutorials</h1>
      {tutorials.length === 0 ? (
        <div className="card">No tutorials available</div>
      ) : (
        <ul>
          {tutorials.map((tut) => (
            <li key={tut.id}>
              <Link to={`/tutorials/${tut.id}`} className="card">
                {tut.title}
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
