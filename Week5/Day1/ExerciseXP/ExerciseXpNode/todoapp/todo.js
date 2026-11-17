export class TodoList {
    constructor() {
        this.tasks = [];
    }

    addTask(id, title) {
        this.tasks.push({
            id,
            title,
            completed: false
        });
    }

    listTasks() {
        return this.tasks;
    }

    markTaskComplete(taskId) {
        const task = this.tasks.find(t => t.id === taskId);
        if (task) {
            task.completed = true;
        }
    }
}
