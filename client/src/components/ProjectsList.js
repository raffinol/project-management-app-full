import { useEffect, useState } from "react";

function ProjectsList() {
    const [projects, setProjects] = useState([]);

    useEffect(() => {
        fetch("/projects")
        .then((r) => r.json())
        .then((project) => setProjects(project));
    }, []);

      return (
        <>
          {projects.map((project) => (
          <div key={project.id}>
            <h4>Title: {project.title}</h4>
            <p><b>Description:</b> {project.description}</p>
            <p><b>urgency:</b> {project.urgency}</p>
            <p><b>Start_date:</b> {project.start_date}</p>
            <p><b>due_date:</b> {project.due_date}</p>
          </div>
          ))}
        </>
      );
  }

export default ProjectsList;