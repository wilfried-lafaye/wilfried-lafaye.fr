async function loadEducation() {
  const response = await fetch("data/education.json");
  const education = await response.json();
  const container = document.querySelector("#education-list");

  container.innerHTML = education.map(edu => `
    <div class="education-item">
      <h3>${edu.degree} – ${edu.school} (${edu.years})</h3>
      <p>${edu.description}</p>
    </div>
  `).join('');
}
document.addEventListener("DOMContentLoaded", loadEducation);
