import React, { useEffect, useState } from "react";
import api from "../api";

export default function Tutorials() {
  const [tutorials, setTutorials] = useState([]);

  useEffect(() => {
    api.get("/tutorials/")
      .then(res => setTutorials(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Tutorials</h1>
      <ul>
        {tutorials.map(tut => (
          <li key={tut.id}>{tut.title}</li>
        ))}
      </ul>
    </div>
  );
}
