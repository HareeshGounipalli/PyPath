import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../api";

export default function Tutorials() {
  const [tutorials, setTutorials] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/tutorials/")
      .then((res) => {
        setTutorials(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="card">Loading tutorials...</div>;
  }

  if (tutorials.length === 0) {
    return <div className="card">No tutorials available</div>;
  }

  return (
    <div>
      <h1>Tutorials</h1>
      <ul>
        {tutorials.map((tut) => {
          // Check if your API returns 'id' or '_id'
          const tutorialId = tut.id || tut._id;
          return (
            <li key={tutorialId}>
              <Link to={`/tutorials/${tutorialId}`} className="card">
                {tut.title}
              </Link>
            </li>
          );
        })}
      </ul>
    </div>
  );
}
