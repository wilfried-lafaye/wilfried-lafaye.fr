async function loadExperience() {
  const response = await fetch("data/experience.json");
  const experience = await response.json();
  const container = document.querySelector("#experience-list");

  container.innerHTML = experience.map(exp => `
    <div class="experience-item">
      <h3>${exp.years} – ${exp.title} @ ${exp.company}</h3>
      <p>${exp.description}</p>
    </div>
  `).join('');
}
document.addEventListener("DOMContentLoaded", loadExperience);
