async function loadSkills() {
  const response = await fetch("data/skills.json");
  const skills = await response.json();
  const container = document.querySelector("#skills-list");

  container.innerHTML = skills.map(skill => `<div class="skill-tag">${skill}</div>`).join('');
}
document.addEventListener("DOMContentLoaded", loadSkills);
