const CATEGORY_COLORS = {
  professional: { bg: 'rgba(59, 130, 246, 0.15)', color: '#60a5fa', label: 'Professional' },
  personal: { bg: 'rgba(34, 197, 94, 0.15)', color: '#4ade80', label: 'Personal' },
  educational: { bg: 'rgba(251, 146, 60, 0.15)', color: '#fb923c', label: 'Educational' }
};

function animateCounter(el, target) {
  let current = 0;
  const duration = 800;
  const step = Math.max(16, Math.floor(duration / target));
  const timer = setInterval(() => {
    current++;
    el.textContent = current;
    if (current >= target) clearInterval(timer);
  }, step);
}

async function loadProjects() {
  const response = await fetch("data/projects.json");
  const projects = await response.json();
  const container = document.querySelector("#projects-list");

  container.innerHTML = projects.map(project => {
    const cat = CATEGORY_COLORS[project.category] || { bg: 'rgba(255,255,255,0.1)', color: '#aaa', label: project.category };
    const techCount = project.technologies ? project.technologies.length : 0;

    const techPills = project.technologies ? project.technologies.map(t =>
      `<span class="tag">${t}</span>`
    ).join('') : '';

    return `
  <div class="project-card">
    <div class="card-top-row">
      <span class="tag category-badge" style="background:${cat.bg};color:${cat.color}">${cat.label}</span>
      <span class="project-date">${project.date || ''}</span>
    </div>
    <h3>${project.title}</h3>
    <p>${project.description}</p>
    <div class="project-stats">
      <div class="stat-item">
        <span class="stat-number" data-target="${techCount}">0</span>
        <span class="stat-label">Technologies</span>
      </div>
    </div>
    <div class="tags">${techPills}</div>
    <a href="${project.link}" class="btn-secondary" aria-label="View details for ${project.title}" style="margin-top:auto;">View Project &rarr;</a>
  </div>`;
  }).join('');

  // Animate counters when cards scroll into view
  const counters = container.querySelectorAll('.stat-number');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = parseInt(entry.target.dataset.target, 10);
        animateCounter(entry.target, target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  counters.forEach(c => observer.observe(c));
}

document.addEventListener("DOMContentLoaded", loadProjects);
