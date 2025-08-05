// --- CÓDIGO MODIFICADO ---
document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('resource-container');
    const searchInput = document.getElementById('searchInput');
    const filterContainer = document.getElementById('filter-container');
    
    if (!container) return; // No ejecutar si no estamos en la página principal

    let allResources = [];
    // Cambiado 'Todos' a 'All'
    let activeFilters = {
        type: 'All',
        level: 'All'
    };

    fetch('/api/resources')
        .then(response => response.json())
        .then(data => {
            if (data.error) throw new Error(data.error);
            allResources = data;
            createFilterButtons(allResources);
            renderResources(allResources);
        })
        .catch(error => {
            console.error('Error al cargar los recursos:', error);
            container.innerHTML = `<p class="error-message">Ocurrió un error al cargar los recursos.</p>`;
        });

    function renderResources(resources) {
        container.innerHTML = '';
        if (resources.length === 0) {
            container.innerHTML = '<p class="info-message">No se encontraron recursos que coincidan con tu búsqueda.</p>';
            return;
        }
        resources.forEach(resource => {
            const card = document.createElement('article');
            card.className = 'resource-card';
            
            const technologiesHtml = resource.technologies.map(tech => `<span class="tag tech-tag">${tech}</span>`).join('');

            card.innerHTML = `
                <h3 class="card-title">
                    <a href="${resource.link}" target="_blank" rel="noopener noreferrer">${resource.name}</a>
                </h3>
                <p class="card-description">${resource.description}</p>
                <div class="card-footer">
                    <span class="tag type-tag">${resource.type}</span>
                    <span class="tag level-tag level-${resource.level.toLowerCase()}">${resource.level}</span>
                </div>
                <div class="technologies">${technologiesHtml}</div>
            `;
            container.appendChild(card);
        });
    }

    function applyFilters() {
        const searchTerm = searchInput.value.toLowerCase();
        
        let filteredResources = allResources.filter(resource => {
            const matchesSearch = searchTerm === '' ||
                resource.name.toLowerCase().includes(searchTerm) ||
                resource.description.toLowerCase().includes(searchTerm) ||
                resource.technologies.some(tech => tech.toLowerCase().includes(searchTerm));

            // Cambiado 'Todos' a 'All' en la condición
            const matchesType = activeFilters.type === 'All' || resource.type === activeFilters.type;
            const matchesLevel = activeFilters.level === 'All' || resource.level === activeFilters.level;

            return matchesSearch && matchesType && matchesLevel;
        });

        renderResources(filteredResources);
    }
    
    function createFilterButtons(resources) {
        // Cambiado 'Todos' a 'All' para el valor por defecto de los botones
        const types = ['All', ...new Set(resources.map(r => r.type).filter(Boolean))];
        const levels = ['All', ...new Set(resources.map(r => r.level).filter(Boolean))];
        
        // Cambiado 'Tipo:' a 'Type:' y 'Nivel:' a 'Level:'
        createButtonGroup('Type:', types, 'type', filterContainer);
        createButtonGroup('Level:', levels, 'level', filterContainer);
    }

    function createButtonGroup(label, options, filterKey, parentElement) {
        const group = document.createElement('div');
        group.className = 'filter-group';
        const labelElement = document.createElement('strong');
        labelElement.className = 'filter-label';
        labelElement.innerText = label;
        group.appendChild(labelElement);
        
        options.forEach(option => {
            const button = document.createElement('button');
            button.className = 'filter-button';
            button.innerText = option;
            // Cambiado 'Todos' a 'All' para marcar el botón activo
            if (option === 'All') button.classList.add('active');
            
            button.addEventListener('click', () => {
                activeFilters[filterKey] = option;
                group.querySelectorAll('.filter-button').forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');
                applyFilters();
            });
            group.appendChild(button);
        });
        parentElement.appendChild(group);
    }

    searchInput.addEventListener('input', applyFilters);
});