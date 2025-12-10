async function loadEducation() {
  const response = await fetch("data/education.json");
  const education = await response.json();
  const container = document.querySelector("#education-list");

  container.innerHTML = education.map(edu => `
    <div class="education-card">
      <h3>${edu.school}</h3>
      <span class="degree">${edu.degree}</span>
      <p class="date">${edu.years}</p>
      <p>${edu.description}</p>
    </div>
  `).join('');
}
document.addEventListener("DOMContentLoaded", loadEducation);
