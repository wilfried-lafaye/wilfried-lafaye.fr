async function loadExperience() {
  const response = await fetch("data/experience.json?v=4");
  const experienceData = await response.json();
  const container = document.querySelector("#experience-list");

  // Output a single wrapper for all roles to float within
  const rolesHtml = experienceData.map((role, index) => {
    // Determine side based on index for desktop (even = left, odd = right)
    const sideClass = (index % 2 === 0) ? 'timeline-left' : 'timeline-right';
    return `
      <div class="experience-role-card ${sideClass}">
        <div class="role-date-badge">${role.years}</div>
        <h3>${role.title}</h3>
        <span class="role">@ ${role.company}</span>
        <p>${role.description}</p>
      </div>
    `;
  }).join('');

  container.innerHTML = `
    <div class="continuous-timeline-container">
      ${rolesHtml}
      <div class="clearfix"></div>
    </div>
  `;
}
document.addEventListener("DOMContentLoaded", loadExperience);
