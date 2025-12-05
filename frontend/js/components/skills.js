async function loadSkills() {
  const response = await fetch("data/skills.json");
  const skills = await response.json();
  const container = document.querySelector("#skills-list");

  container.innerHTML = skills.map(skill => `<li>${skill}</li>`).join('');
}
document.addEventListener("DOMContentLoaded", loadSkills);
