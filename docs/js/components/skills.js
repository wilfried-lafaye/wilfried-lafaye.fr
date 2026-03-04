/**
 * Skills component — simple text-based bubbles
 */
function loadSkills() {
  const skills = {
    "Languages": ["Python", "SQL", "JavaScript", "HTML/CSS"],
    "AI / ML": ["PyTorch", "TensorFlow", "Scikit-learn", "Deep Learning"],
    "Data": ["Pandas", "NumPy", "Data Visualization", "Data Manipulation"],
    "Tools": ["Git", "Docker", "Astro", "GitHub Actions"]
  };

  const container = document.querySelector("#skills-list");
  if (!container) return;

  container.innerHTML = Object.entries(skills).map(([category, items]) => {
    const pills = items.map(skill => `<span class="skill-pill">${skill}</span>`).join('');

    return `
            <div class="skill-group">
                <h3 class="skill-category-title">${category}</h3>
                <div class="skill-pills-container">${pills}</div>
            </div>
        `;
  }).join('');
}

// Immediate execution with fallback
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', loadSkills);
} else {
  loadSkills();
}
