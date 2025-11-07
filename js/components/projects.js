async function loadProjects() {
  const response = await fetch("data/projects.json");
  const projects = await response.json();
  const container = document.querySelector("#projects-list");

  container.innerHTML = projects.map(project => `
    <div class="project-card">
      <h3>${project.title}</h3>
      <p>${project.description}</p>
      <a href="${project.link}" class="project-link">View Details</a>
    </div>
  `).join('');
}
document.addEventListener("DOMContentLoaded", loadProjects);
