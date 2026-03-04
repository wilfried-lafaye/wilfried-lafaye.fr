async function loadExperience() {
  const response = await fetch("data/experience.json?v=6");
  const data = await response.json();
  const container = document.querySelector("#experience-list");

  function renderRoles(roles) {
    if (!roles || roles.length === 0) return '';
    return roles.map(role => `
      <div class="fresco-card">
        <h3>${role.title}</h3>
        <span class="role">@ ${role.company}</span>
        <p>${role.description}</p>
      </div>
    `).join('');
  }

  function renderBracket(node) {
    const startHtml = renderRoles(node.roles_start);
    const endHtml = renderRoles(node.roles_end);

    let nestedHtml = '';
    if (node.nested && node.nested.length > 0) {
      nestedHtml = `<div class="fresco-nested">` + node.nested.map(renderBracket).join('') + `</div>`;
    }

    return `
      <div class="fresco-bracket">
        <div class="fresco-badge">${node.period}</div>
        <div class="fresco-content">
           ${startHtml}
           ${nestedHtml}
           ${endHtml}
        </div>
      </div>
    `;
  }

  // Clear previous classes and add the container class directly to the structure
  container.className = "";
  container.innerHTML = `<div class="fresco-container">` + data.map(renderBracket).join('') + `</div>`;
}
document.addEventListener("DOMContentLoaded", loadExperience);
