const CATEGORY_COLORS = {
  professional: { bg: 'rgba(59, 130, 246, 0.15)', color: '#60a5fa', label: 'Professional' },
  personal: { bg: 'rgba(34, 197, 94, 0.15)', color: '#4ade80', label: 'Personal' },
  educational: { bg: 'rgba(251, 146, 60, 0.15)', color: '#fb923c', label: 'Educational' }
};

async function loadProjects() {
  const response = await fetch("data/projects.json");
  const projects = await response.json();
  const container = document.querySelector("#projects-list");

  container.innerHTML = projects.map(project => {
    const cat = CATEGORY_COLORS[project.category] || { bg: 'rgba(255,255,255,0.1)', color: '#aaa', label: project.category };
    return `
  <div class="project-card">
    <div class="tags">
      <span class="tag category-badge" style="background:${cat.bg};color:${cat.color}">${cat.label}</span>
    </div>
    <h3>${project.title}</h3>
    <p>${project.description}</p>
    <a href="${project.link}" class="btn-secondary" aria-label="View details for ${project.title}" style="margin-top:auto;">View Project &rarr;</a>
  </div>`;
  }).join('');
}
document.addEventListener("DOMContentLoaded", loadProjects);
