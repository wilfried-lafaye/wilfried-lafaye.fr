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

        // Sort by date descending
        data.sort((a, b) => {
            const dateA = a.date ? new Date(a.date) : new Date(0);
            const dateB = b.date ? new Date(b.date) : new Date(0);
            return dateB - dateA;
        });

        let currentYear = null;
        let currentGrid = null;

        data.forEach(project => {
            // Safe date parsing
            const projectDate = project.date ? new Date(project.date) : new Date();
            const projectYear = projectDate.getFullYear();

            // If Year changes, create new heading and grid
            if (projectYear !== currentYear) {
                currentYear = projectYear;

                // Year Heading
                const yearHeading = document.createElement("h2");
                yearHeading.textContent = currentYear;
                yearHeading.style.marginTop = "3rem";
                yearHeading.style.marginBottom = "1.5rem";
                yearHeading.style.borderBottom = "1px solid rgba(255,255,255,0.1)";
                yearHeading.style.paddingBottom = "0.5rem";
                yearHeading.style.color = "var(--text-primary)";
                listContainer.appendChild(yearHeading);

                // Grid Container for this year
                currentGrid = document.createElement("div");
                currentGrid.className = "grid-container";
                listContainer.appendChild(currentGrid);
            }

            const card = document.createElement("div");
            card.className = "project-card";

            // Create tags HTML
            const tagsHtml = project.technologies
                ? project.technologies.slice(0, 3).map(tech => `<span class="tag">${tech}</span>`).join('')
                : '';

            const categoryLabel = project.category
                ? `<span class="category-badge ${project.category}">${project.category}</span>`
                : '';

            // Format Month Year
            const dateStr = projectDate.toLocaleDateString('en-US', { month: 'short', year: 'numeric' });

            card.innerHTML = `
        <div class="card-header">
           ${categoryLabel}
           <div class="tech-tags">${tagsHtml}</div>
        </div>
        <h3>${project.title}</h3>
        <p>${project.description}</p>
        <div style="display:flex; justify-content:flex-end; align-items:center; margin-top: auto;">
            <a href="${project.link}" class="btn-secondary">View Project &rarr;</a>
        </div>
      `;

            currentGrid.appendChild(card);
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
