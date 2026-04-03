document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskList = document.getElementById('task-list');
    const emptyState = document.getElementById('empty-state');
    const editModal = document.getElementById('edit-modal');
    const editForm = document.getElementById('edit-form');
    const closeBtn = document.querySelector('.close-btn');

    // Fetch and display all tasks
    async function loadTasks() {
        try {
            const response = await fetch('/api/tasks/');
            const tasks = await response.json();
            
            taskList.innerHTML = '';
            
            if (tasks.length === 0) {
                emptyState.style.display = 'block';
            } else {
                emptyState.style.display = 'none';
                tasks.forEach(task => {
                    renderTask(task);
                });
            }
        } catch (error) {
            console.error('Error loading tasks:', error);
            alert('Failed to load tasks. Please try again later.');
        }
    }

    // Render a single task card
    function renderTask(task) {
        const item = document.createElement('li');
        item.className = `task-item ${task.status}`;
        item.id = `task-${task.id}`;
        
        const dueDate = new Date(task.due_date);
        const formattedDate = dueDate.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });

        item.innerHTML = `
            <div class="task-info">
                <div class="task-title">
                    ${task.title}
                    <span class="status-badge status-${task.status}">${task.status}</span>
                </div>
                <div class="task-desc">${task.description || 'No description provided'}</div>
                <div class="task-meta">Due: ${formattedDate}</div>
            </div>
            <div class="task-actions">
                <button class="btn-small btn-edit" data-id="${task.id}" title="Edit Task">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
                </button>
                ${task.status === 'Pending' ? `
                    <button class="btn-small btn-complete" data-id="${task.id}" title="Mark as Completed">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    </button>
                ` : ''}
                <button class="btn-small btn-delete" data-id="${task.id}" title="Delete Task">
                     <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg>
                </button>
            </div>
        `;
        
        taskList.appendChild(item);

        // Event listeners for actions
        item.querySelector('.btn-edit').addEventListener('click', () => openEditModal(task));

        const completeBtn = item.querySelector('.btn-complete');
        if (completeBtn) {
            completeBtn.addEventListener('click', () => updateTaskStatus(task.id, 'Completed'));
        }
        
        item.querySelector('.btn-delete').addEventListener('click', () => deleteTask(task.id));
    }

    function openEditModal(task) {
        document.getElementById('edit-task-id').value = task.id;
        document.getElementById('edit-title').value = task.title;
        document.getElementById('edit-description').value = task.description || '';
        
        // Format date for datetime-local input (YYYY-MM-DDTHH:MM)
        const date = new Date(task.due_date);
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');
        document.getElementById('edit-due_date').value = `${year}-${month}-${day}T${hours}:${minutes}`;
        document.getElementById('edit-status').value = task.status;
        
        editModal.style.display = 'flex';
    }

    closeBtn.onclick = () => editModal.style.display = 'none';
    window.onclick = (e) => { if (e.target == editModal) editModal.style.display = 'none'; };

    editForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const id = document.getElementById('edit-task-id').value;
        const formData = new FormData(editForm);
        const data = {
            title: formData.get('title'),
            description: formData.get('description'),
            due_date: formData.get('due_date'),
            status: formData.get('status')
        };

        try {
            const response = await fetch(`/api/tasks/${id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                editModal.style.display = 'none';
                loadTasks();
            }
        } catch (error) {
            console.error('Error updating task:', error);
        }
    });

    // Handle form submission to create task
    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(taskForm);
        const data = {
            title: formData.get('title'),
            description: formData.get('description'),
            due_date: formData.get('due_date'),
            status: 'Pending'
        };

        try {
            const response = await fetch('/api/tasks/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                const newTask = await response.json();
                taskForm.reset();
                loadTasks(); // Reload all to keep sorting
            } else {
                const err = await response.json();
                alert(`Error: ${JSON.stringify(err)}`);
            }
        } catch (error) {
            console.error('Error creating task:', error);
            alert('Failed to connect to API.');
        }
    });

    // Update task status
    async function updateTaskStatus(id, newStatus) {
        try {
            const response = await fetch(`/api/tasks/${id}/`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ status: newStatus })
            });

            if (response.ok) {
                loadTasks();
            }
        } catch (error) {
            console.error('Error updating task:', error);
        }
    }

    // Delete task
    async function deleteTask(id) {
        try {
            const response = await fetch(`/api/tasks/${id}/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });

            if (response.ok) {
                loadTasks();
            }
        } catch (error) {
            console.error('Error deleting task:', error);
        }
    }

    // CSRF helper
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Initial load
    loadTasks();
});
