"use client";

import React, { useState, useEffect, useCallback } from 'react';
import { todoApi, Task } from '@/lib/api';
import { 
    CheckCircle2, 
    Circle, 
    Trash2, 
    Edit2, 
    Plus, 
    Calendar, 
    Save, 
    X, 
    Loader2 
} from 'lucide-react';

export default function TaskList() {
    const [tasks, setTasks] = useState<Task[]>([]);
    const [newTaskTitle, setNewTaskTitle] = useState('');
    const [newTaskDesc, setNewTaskDesc] = useState('');
    const [filter, setFilter] = useState('all');
    const [isLoading, setIsLoading] = useState(false);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [editingParams, setEditingParams] = useState<{ id: number, title: string, description: string } | null>(null);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);

    const loadTasks = useCallback(async () => {
        setIsLoading(true);
        try {
            const data = await todoApi.getTasks(filter === 'all' ? undefined : filter);
            setTasks(data);
            setErrorMessage(null);
        } catch (error) {
            console.error('Failed to load tasks', error);
            setErrorMessage(`Failed to load tasks. Backend may be offline.`);
        } finally {
            setIsLoading(false);
        }
    }, [filter]);

    useEffect(() => {
        loadTasks();
    }, [loadTasks]);

    const handleAddTask = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        
        if (!newTaskTitle.trim()) {
            setErrorMessage('Title is required.');
            return;
        }

        setIsSubmitting(true);
        setErrorMessage(null);
        try {
            await todoApi.createTask(newTaskTitle, newTaskDesc);
            setNewTaskTitle('');
            setNewTaskDesc('');
            await loadTasks(); 
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        } catch (error: any) {
            console.error('Failed to create task', error);
            const msg = error.response?.data?.detail || "Could not connect to server.";
            setErrorMessage(`Failed to create task: ${msg}`);
        } finally {
            setIsSubmitting(false);
        }
    };

    const handleToggle = async (id: number) => {
        try {
            // FIX: Ensure this calls the correct backend route with trailing slash
            await todoApi.toggleComplete(id);
            await loadTasks();
        } catch (error) {
            console.error('Failed to toggle task', error);
            setErrorMessage('Failed to update task status.');
        }
    };

    const handleDelete = async (id: number) => {
        if (!confirm('Are you sure you want to delete this task?')) return;
        try {
            await todoApi.deleteTask(id);
            await loadTasks();
        } catch (error) {
            console.error('Failed to delete task', error);
            setErrorMessage('Failed to delete task.');
        }
    };

    const handleUpdate = async () => {
        if (!editingParams) return;
        try {
            await todoApi.updateTask(editingParams.id, {
                title: editingParams.title,
                description: editingParams.description
            });
            setEditingParams(null);
            await loadTasks();
        } catch (error) {
            console.error("Failed to update task", error);
            setErrorMessage('Failed to update task.');
        }
    };

    return (
        <div className="max-w-4xl mx-auto px-4 py-6 sm:px-6 font-sans">
            {/* Header and Filters */}
            <div className="flex flex-col gap-4 sm:flex-row sm:justify-between sm:items-center mb-6">
                <h1 className="text-3xl font-bold text-gray-800 dark:text-white">My Tasks</h1>
                <div className="flex gap-2 overflow-x-auto pb-1">
                    {['all', 'pending', 'completed'].map(f => (
                        <button
                            key={f}
                            onClick={() => setFilter(f)}
                            className={`px-4 py-2 rounded-full capitalize text-sm font-medium transition-all ${
                                filter === f 
                                ? 'bg-blue-600 text-white shadow-lg shadow-blue-500/30' 
                                : 'bg-white dark:bg-gray-800 text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 border border-gray-200 dark:border-gray-700'
                            }`}
                        >
                            {f}
                        </button>
                    ))}
                </div>
            </div>

            {/* Add Task Form */}
            <form onSubmit={handleAddTask} className="mb-8 p-6 bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700">
                <div className="flex flex-col gap-4">
                    <input
                        id="task-title-input"
                        name="task-title"
                        type="text"
                        value={newTaskTitle}
                        onChange={(e) => setNewTaskTitle(e.target.value)}
                        placeholder="What needs to be done?"
                        disabled={isSubmitting}
                        className="text-lg font-medium placeholder:text-gray-400 dark:placeholder:text-gray-500 border-none focus:ring-0 p-0 text-black dark:text-white bg-transparent outline-none"
                    />
                    <textarea
                        id="task-desc-input"
                        name="task-description"
                        value={newTaskDesc}
                        onChange={(e) => setNewTaskDesc(e.target.value)}
                        placeholder="Add a description..."
                        disabled={isSubmitting}
                        className="text-sm text-gray-600 dark:text-gray-300 placeholder:text-gray-400 dark:placeholder:text-gray-500 border-none focus:ring-0 p-0 resize-none h-10 bg-transparent outline-none"
                    />
                    <div className="flex justify-between items-center pt-2 border-t border-gray-100 dark:border-gray-700">
                        <div className="flex-1">
                             {errorMessage && <p className="text-xs text-red-500">{errorMessage}</p>}
                        </div>
                        <button 
                            type="submit" 
                            disabled={isSubmitting || !newTaskTitle.trim()}
                            className="w-full sm:w-auto flex items-center justify-center gap-2 bg-black dark:bg-white text-white dark:text-black px-6 py-2 rounded-full hover:bg-gray-800 dark:hover:bg-gray-200 transition-all font-medium disabled:opacity-30 disabled:cursor-not-allowed"
                        >
                            {isSubmitting ? <Loader2 size={18} className="animate-spin" /> : <Plus size={18} />}
                            {isSubmitting ? 'Adding...' : 'Add Task'}
                        </button>
                    </div>
                </div>
            </form>

            {/* Task List */}
            <div className="grid gap-4">
                {isLoading && tasks.length === 0 ? (
                    <div className="flex justify-center py-10"><Loader2 className="animate-spin text-blue-500" /></div>
                ) : (
                    tasks.map((task) => (
                        <div key={task.id} className={`group bg-white dark:bg-gray-800 p-5 rounded-2xl border transition-all hover:shadow-md ${task.completed ? 'border-gray-100 dark:border-gray-800 bg-gray-50/50 dark:bg-gray-800/50' : 'border-gray-200 dark:border-gray-700'}`}>
                            {editingParams && editingParams.id === task.id ? (
                                <div className="flex flex-col gap-3">
                                    <input
                                        className="font-bold text-lg border dark:border-gray-600 p-2 rounded bg-white dark:bg-gray-700 text-black dark:text-white outline-blue-500"
                                        value={editingParams.title}
                                        onChange={(e) => setEditingParams({ ...editingParams!, title: e.target.value })}
                                        autoFocus
                                    />
                                    <textarea
                                        className="text-gray-600 dark:text-gray-300 border dark:border-gray-600 p-2 rounded bg-white dark:bg-gray-700 outline-blue-500"
                                        value={editingParams.description || ''}
                                        onChange={(e) => setEditingParams({ ...editingParams!, description: e.target.value })}
                                    />
                                    <div className="flex gap-2 justify-end">
                                        <button onClick={() => setEditingParams(null)} className="p-2 text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full">
                                            <X size={20} />
                                        </button>
                                        <button onClick={handleUpdate} className="p-2 text-blue-600 hover:bg-blue-50 dark:hover:bg-blue-900/30 rounded-full">
                                            <Save size={20} />
                                        </button>
                                    </div>
                                </div>
                            ) : (
                                <div className="flex items-start gap-4">
                                    <button
                                        onClick={() => handleToggle(task.id!)}
                                        className={`mt-1 flex-shrink-0 transition-colors ${task.completed ? 'text-green-500' : 'text-gray-300 dark:text-gray-600 hover:text-blue-500'}`}
                                    >
                                        {task.completed ? <CheckCircle2 size={24} /> : <Circle size={24} />}
                                    </button>

                                    <div className="flex-1 min-w-0">
                                        <h3 className={`text-lg font-semibold mb-1 truncate ${task.completed ? 'text-gray-400 dark:text-gray-500 line-through' : 'text-gray-800 dark:text-white'}`}>
                                            {task.title}
                                        </h3>
                                        {task.description && (
                                            <p className="text-gray-500 dark:text-gray-400 text-sm line-clamp-2">{task.description}</p>
                                        )}
                                        <div className="flex items-center gap-4 mt-3 text-xs text-gray-400 dark:text-gray-500">
                                            <span className="flex items-center gap-1">
                                                <Calendar size={12} />
                                                {task.created_at ? new Date(task.created_at).toLocaleDateString() : '—'}
                                            </span>
                                        </div>
                                    </div>

                                    <div className="flex items-center gap-1 opacity-100 lg:opacity-0 lg:group-hover:opacity-100 transition-opacity">
                                        <button
                                            onClick={() => setEditingParams({ id: task.id!, title: task.title, description: task.description || '' })}
                                            className="p-2 text-gray-400 hover:text-blue-600 hover:bg-blue-50 dark:hover:bg-blue-900/30 rounded-full transition-colors"
                                        >
                                            <Edit2 size={18} />
                                        </button>
                                        <button
                                            onClick={() => handleDelete(task.id!)}
                                            className="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-900/30 rounded-full transition-colors"
                                        >
                                            <Trash2 size={18} />
                                        </button>
                                    </div>
                                </div>
                            )}
                        </div>
                    ))
                )}
                
                {!isLoading && tasks.length === 0 && (
                    <div className="text-center py-20 bg-gray-50 dark:bg-gray-800/50 rounded-2xl border border-dashed border-gray-200 dark:border-gray-700">
                        <p className="text-gray-500 dark:text-gray-400">
                            {filter === 'all' && "No tasks found. Add one above!"}
                            {filter === 'pending' && "No pending tasks! Good job!"}
                            {filter === 'completed' && "No completed tasks yet. Keep going!"}
                        </p>
                    </div>
                )}
            </div>
        </div>
    );
}