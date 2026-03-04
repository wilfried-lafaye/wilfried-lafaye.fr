async function loadExperience() {
  const response = await fetch("data/experience.json?v=2");
  const experienceData = await response.json();
  const container = document.querySelector("#experience-list");

  container.innerHTML = experienceData.map(periodData => {
    // Generate inner cards for each role in this period
    const rolesHtml = periodData.roles.map(role => `
      <div class="experience-role-card">
        <h3>${role.title}</h3>
        <span class="role">@ ${role.company}</span>
        <p>${role.description}</p>
      </div>
    `).join('');

    // Outer container represents the period node on the timeline
    return `
      <div class="experience-card period-group">
        <div class="period-badge">${periodData.period}</div>
        <div class="period-roles">
          ${rolesHtml}
        </div>
      </div>
    `;
  }).join('');
}
document.addEventListener("DOMContentLoaded", loadExperience);
