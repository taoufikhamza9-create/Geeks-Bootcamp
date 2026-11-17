import { TodoList } from './todo.js';  
const todoList = new TodoList();
todoList.addTask(1, 'Learn JavaScript');
todoList.addTask(2, 'Build a todo app');
todoList.addTask(3, 'Test the app');
todoList.markTaskComplete(2);
console.log(todoList.listTasks());
