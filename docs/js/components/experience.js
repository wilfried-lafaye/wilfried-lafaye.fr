async function loadExperience() {
  const response = await fetch("data/experience.json?v=3");
  const experienceData = await response.json();
  const container = document.querySelector("#experience-list");

  container.innerHTML = experienceData.map(periodData => {
    // Generate inner cards for each role in this period
    const rolesHtml = periodData.roles.map((role, index) => {
      // Determine side based on index for desktop (even = left, odd = right)
      const sideClass = (index % 2 === 0) ? 'timeline-left' : 'timeline-right';
      return `
        <div class="experience-role-card ${sideClass}">
          <h3>${role.title}</h3>
          <span class="role">@ ${role.company}</span>
          <p>${role.description}</p>
        </div>
      `;
    }).join('');

    // Outer container represents the period node on the timeline
    return `
      <div class="period-group">
        <div class="timeline-center-node">
          <div class="period-badge">${periodData.period}</div>
        </div>
        <div class="period-roles-container">
          ${rolesHtml}
          <div class="clearfix"></div>
        </div>
      </div>
    `;
  }).join('');
}
document.addEventListener("DOMContentLoaded", loadExperience);
