import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api"; // make sure this exists

export default function TutorialDetail() {
  const { id } = useParams();
  const [tutorial, setTutorial] = useState(null);

  useEffect(() => {
    api.get(`/tutorials/${id}`)
      .then(res => setTutorial(res.data))
      .catch(err => console.error(err));
  }, [id]);

  if (!tutorial) return <p>Loading...</p>;

  return (
    <div>
      <h1>{tutorial.title}</h1>
      <p>{tutorial.description}</p>
      {tutorial.lessons.map(lesson => (
        <div key={lesson.id}>
          <h3>{lesson.title}</h3>
          <p>{lesson.content}</p>
        </div>
      ))}
    </div>
  );
}
