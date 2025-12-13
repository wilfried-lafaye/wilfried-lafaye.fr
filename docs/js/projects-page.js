document.addEventListener("DOMContentLoaded", async () => {
    const listContainer = document.getElementById("projects-grid");
    const searchInput = document.getElementById("search-input");
    const filterButtons = document.querySelectorAll(".filter-btn");

    let projects = [];
    let currentFilter = "all";

    // Fetch projects
    try {
        const response = await fetch("data/projects.json");
        projects = await response.json();
        renderProjects(projects);
    } catch (error) {
        console.error("Error loading projects:", error);
        listContainer.innerHTML = "<p>Failed to load projects.</p>";
    }

    // Render Projects
    function renderProjects(data) {
        listContainer.innerHTML = "";

        if (data.length === 0) {
            listContainer.innerHTML = "<p>No projects found.</p>";
            return;
        }

        data.forEach(project => {
            const card = document.createElement("div");
            card.className = "project-card";

            // Create tags HTML
            const tagsHtml = project.technologies
                ? project.technologies.slice(0, 3).map(tech => `<span class="tag">${tech}</span>`).join('')
                : '';

            const categoryLabel = project.category
                ? `<span class="category-badge ${project.category}">${project.category}</span>`
                : '';

            card.innerHTML = `
        <div class="card-header">
           ${categoryLabel}
           <div class="tech-tags">${tagsHtml}</div>
        </div>
        <h3>${project.title}</h3>
        <p>${project.description}</p>
        <a href="${project.link}" class="btn-secondary">View Project &rarr;</a>
      `;

            listContainer.appendChild(card);
        });
    }

    // Filter Logic
    function filterProjects() {
        const query = searchInput.value.toLowerCase();

        const filtered = projects.filter(project => {
            const matchesSearch = project.title.toLowerCase().includes(query) ||
                project.description.toLowerCase().includes(query);
            const matchesCategory = currentFilter === "all" || project.category === currentFilter;

            return matchesSearch && matchesCategory;
        });

        renderProjects(filtered);
    }

    // Event Listeners
    searchInput.addEventListener("input", filterProjects);

    filterButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            // Update active button state
            filterButtons.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");

            // Update filter and re-render
            currentFilter = btn.dataset.filter;
            filterProjects();
        });
    });
});
