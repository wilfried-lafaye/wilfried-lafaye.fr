async function loadExperience() {
  const response = await fetch("data/experience.json");
  const experience = await response.json();
  const container = document.querySelector("#experience-list");

  container.innerHTML = experience.map(exp => `
    <div class="experience-card">
      <h3>${exp.title}</h3>
      <span class="role">@ ${exp.company}</span>
      <p class="date">${exp.years}</p>
      <p>${exp.description}</p>
    </div>
  `).join('');
}
document.addEventListener("DOMContentLoaded", loadExperience);
