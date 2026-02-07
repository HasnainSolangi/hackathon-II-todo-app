import axios from 'axios';
import { authClient } from './auth-client';

const getApiBaseUrl = () => {
    if (process.env.NEXT_PUBLIC_API_URL) {
        return process.env.NEXT_PUBLIC_API_URL;
    }
    if (typeof window !== 'undefined') {
        const host = window.location.hostname === 'localhost' ? '127.0.0.1' : window.location.hostname;
        return `http://${host}:8000/api`;
    }
    return 'http://localhost:8000/api';
};

const API_URL = getApiBaseUrl();
export const API_BASE_URL = API_URL;

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
    withCredentials: true,
});

// TYPES
export interface Task {
    id?: number;
    user_id: string;
    title: string;
    description?: string;
    completed: boolean;
    created_at?: string;
}

type SessionResponse = {
    data?: {
        session?: {
            token?: string;
        };
        token?: string;
    };
};

// REQUEST INTERCEPTOR: The "Token Fix"
api.interceptors.request.use(async (config) => {
    if (typeof window !== 'undefined') {
        try {
            // 1. Try to get the session from Better Auth Client
            const session = await authClient.getSession() as SessionResponse;
            
            // 2. Better Auth can nest the token in different places depending on version
            const token = session?.data?.session?.token || session?.data?.token;

            // 3. Fallback: If the client hasn't loaded, check the cookie/local storage key
            const fallbackToken = document.cookie
                .split('; ')
                .find(row => row.startsWith('better-auth.session_token='))
                ?.split('=')[1];

            const bearer = token || fallbackToken;

            if (bearer) {
                config.headers.Authorization = `Bearer ${bearer}`;
            }
        } catch (e) {
            console.error("Auth Interceptor Error:", e);
        }
    }
    return config;
}, (error) => Promise.reject(error));

// API METHODS
export const todoApi = {
    getTasks: async (status?: string) => {
        // FIX: Match the backend query parameter name 'task_status'
        const params = status && status !== 'all' ? { task_status: status } : {};
        const response = await api.get<Task[]>('/tasks/', { params });
        return response.data;
    },

    createTask: async (title: string, description?: string) => {
        // Ensure trailing slash matches FastAPI router
        const response = await api.post<Task>('/tasks/', { title, description });
        return response.data;
    },

    updateTask: async (id: number, data: Partial<Task>) => {
        const response = await api.put<Task>(`/tasks/${id}/`, data);
        return response.data;
    },

    toggleComplete: async (id: number) => {
        // Ensure trailing slash for toggle endpoint
        const response = await api.patch<Task>(`/tasks/${id}/complete/`);
        return response.data;
    },

    deleteTask: async (id: number) => {
        const response = await api.delete(`/tasks/${id}/`);
        return response.data;
    }
};