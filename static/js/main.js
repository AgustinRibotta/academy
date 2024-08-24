document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('course-search');
    const searchResults = document.getElementById('search-results');

    searchInput.addEventListener('input', function() {
        const query = searchInput.value;

        if (query.length >= 2) {  // Solo buscar si la consulta tiene al menos 2 caracteres
            fetch(`/courses/search/?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    const results = data.results;
                    searchResults.innerHTML = '';  // Limpiar resultados anteriores

                    if (results.length > 0) {
                        results.forEach(course => {
                            const courseElement = document.createElement('div');
                            courseElement.className = 'col-md-4 mb-4';
                            courseElement.innerHTML = `
                                <div class="card shadow-sm border-light">
                                    <div class="card-body">
                                        <h5 class="card-title">${course.name}</h5>
                                        <p class="card-text">${course.description.slice(0, 150)}${course.description.length > 150 ? '...' : ''}</p>
                                        <a href="/courses/${course.id}" class="btn btn-primary">View Details</a>
                                    </div>
                                </div>
                            `;
                            searchResults.appendChild(courseElement);
                        });
                    } else {
                        searchResults.innerHTML = '<p class="text-center">No courses found.</p>';
                    }
                });
        } else {
            searchResults.innerHTML = '';  // Limpiar resultados si la consulta es demasiado corta
        }
    });
});
