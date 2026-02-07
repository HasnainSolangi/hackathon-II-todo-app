"use client";
import { useState, useEffect } from 'react';
import TaskList from '@/components/TaskList';
import Auth from '@/components/Auth';
import { authClient } from '@/lib/auth-client';
import { ArrowRight, Layout, Zap, Layers, BookOpen } from 'lucide-react';
import Link from 'next/link';

interface Session {
  user: {
    email: string;
  };
}

export default function Home() {
  const [session, setSession] = useState<Session | null>(null);
  const [showAuth, setShowAuth] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function checkSession() {
      try {
        const { data } = await authClient.getSession();
        setSession(data);
      } catch { } finally {
        setLoading(false);
      }
    }
    checkSession();
  }, []);

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center bg-white">
      <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-black"></div>
    </div>
  );

  if (session) {
    return (
      <main className="min-h-screen bg-gray-50">
        <nav className="bg-white border-b border-gray-100 sticky top-0 z-10">
          <div className="max-w-6xl mx-auto px-4 py-3 sm:py-0 sm:h-16 flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
            <Link href="/" className="font-bold text-xl tracking-tight text-black dark:text-white hover:opacity-80 transition-opacity">Todo.</Link>
            <div className="flex flex-wrap items-center gap-2 sm:gap-4">
              <span className="text-xs sm:text-sm font-medium text-gray-600 break-all">{session.user.email}</span>
              <button
                onClick={() => authClient.signOut().then(() => window.location.reload())}
                className="text-xs sm:text-sm font-medium text-red-500 hover:bg-red-50 px-3 py-1.5 rounded-full transition-colors"
              >
                Sign Out
              </button>
            </div>
          </div>
        </nav>
        <div className="py-8">
          <TaskList />
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-white">
      {/* Navigation */}
      <nav className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
<Link href="/" className="font-bold text-2xl tracking-tighter hover:opacity-80 transition-opacity">Todo.</Link>
      </nav>

      {/* Hero Section */}
      <div className="max-w-7xl mx-auto px-6 pt-20 pb-32">
        {showAuth ? (
          <div className="max-w-md mx-auto animate-in fade-in slide-in-from-bottom-8 duration-500">
            <div className="mb-8 text-center">
              <button onClick={() => setShowAuth(false)} className="text-sm text-gray-500 hover:text-black mb-4">Back to home</button>
            </div>
            <Auth />
          </div>
        ) : (
          <div className="text-center max-w-3xl mx-auto animate-in fade-in slide-in-from-bottom-8 duration-700">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 text-blue-600 text-xs font-bold uppercase tracking-wider mb-6">
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
              </span>
              Values Hackathon II
            </div>
            <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-gray-900 mb-8 leading-tight">
              Organize your work, <br />
              <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">amplify your impact.</span>
            </h1>
            <p className="text-xl text-gray-500 mb-10 leading-relaxed max-w-2xl mx-auto">
              A powerful, modern todo application built with Next.js 16, FastAPI, and AI-ready architecture. Experience the evolution of task management.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <button
                onClick={() => setShowAuth(true)}
                className="w-full sm:w-auto px-8 py-4 bg-black text-white rounded-full font-medium hover:scale-105 transition-transform flex items-center justify-center gap-2 shadow-xl shadow-black/10"
              >
                Try Free
                <ArrowRight size={18} />
              </button>
              <a href="#how-it-works" className="w-full sm:w-auto px-8 py-4 bg-white dark:bg-gray-800 text-gray-900 dark:text-white border border-gray-200 dark:border-gray-700 rounded-full font-medium hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors shadow-sm flex items-center justify-center">
                Learn More
              </a>
            </div>

            {/* Feature Cards */}
            <div id="features" className="grid md:grid-cols-3 gap-6 mt-24 text-left">
              <div className="p-8 rounded-3xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-gray-200 dark:hover:border-gray-700 transition-colors">
                <div className="w-12 h-12 bg-blue-100 dark:bg-blue-900/30 rounded-xl flex items-center justify-center mb-6 text-blue-600 dark:text-blue-400">
                  <Layout size={24} />
                </div>
                <h3 className="font-bold text-xl mb-3 text-gray-900 dark:text-white">Modern Interface</h3>
                <p className="text-gray-500 dark:text-gray-400 leading-relaxed">Clean, distraction-free design built with Tailwind CSS and Next.js 16.</p>
              </div>
              <div className="p-8 rounded-3xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-gray-200 dark:hover:border-gray-700 transition-colors">
                <div className="w-12 h-12 bg-purple-100 dark:bg-purple-900/30 rounded-xl flex items-center justify-center mb-6 text-purple-600 dark:text-purple-400">
                  <Zap size={24} />
                </div>
                <h3 className="font-bold text-xl mb-3 text-gray-900 dark:text-white">Fast & Secure</h3>
                <p className="text-gray-500 dark:text-gray-400 leading-relaxed">Powered by FastAPI and Better Auth for secure, high-performance interactions.</p>
              </div>
              <div className="p-8 rounded-3xl bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 hover:border-gray-200 dark:hover:border-gray-700 transition-colors">
                <div className="w-12 h-12 bg-green-100 dark:bg-green-900/30 rounded-xl flex items-center justify-center mb-6 text-green-600 dark:text-green-400">
                  <Layers size={24} />
                </div>
                <h3 className="font-bold text-xl mb-3 text-gray-900 dark:text-white">Cloud Ready</h3>
                <p className="text-gray-500 dark:text-gray-400 leading-relaxed">Built on Neon Serverless Postgres for scalable, effortless data management.</p>
              </div>
            </div>

            {/* How It Works Section */}
            <div id="how-it-works" className="mt-32 text-center">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-50 dark:bg-purple-900/20 text-purple-600 dark:text-purple-400 text-xs font-bold uppercase tracking-wider mb-6">
                <BookOpen size={14} />
                Guide
              </div>
              <h2 className="text-3xl md:text-5xl font-bold text-gray-900 dark:text-white mb-16">How to use Todo.</h2>

              <div className="grid md:grid-cols-3 gap-8 relative">
                {/* Connecting Line */}
                <div className="hidden md:block absolute top-1/2 left-0 w-full h-0.5 bg-gradient-to-r from-gray-200 via-gray-300 to-gray-200 dark:from-gray-800 dark:via-gray-700 dark:to-gray-800 -z-10 translate-y-[-50%]"></div>

                <div className="relative bg-white dark:bg-black p-6">
                  <div className="w-16 h-16 mx-auto bg-black dark:bg-white text-white dark:text-black rounded-2xl flex items-center justify-center text-xl font-bold mb-6 shadow-xl">1</div>
                  <h3 className="text-xl font-bold mb-3 dark:text-white">Sign Up</h3>
                  <p className="text-gray-500 dark:text-gray-400">Create an account using Email, Google, or GitHub to start syncing your tasks.</p>
                </div>
                <div className="relative bg-white dark:bg-black p-6">
                  <div className="w-16 h-16 mx-auto bg-black dark:bg-white text-white dark:text-black rounded-2xl flex items-center justify-center text-xl font-bold mb-6 shadow-xl">2</div>
                  <h3 className="text-xl font-bold mb-3 dark:text-white">Create Tasks</h3>
                  <p className="text-gray-500 dark:text-gray-400">Add your daily to-dos, descriptions, and organize your chaotic life.</p>
                </div>
                <div className="relative bg-white dark:bg-black p-6">
                  <div className="w-16 h-16 mx-auto bg-black dark:bg-white text-white dark:text-black rounded-2xl flex items-center justify-center text-xl font-bold mb-6 shadow-xl">3</div>
                  <h3 className="text-xl font-bold mb-3 dark:text-white">Track Progress</h3>
                  <p className="text-gray-500 dark:text-gray-400">Mark tasks as done, filter by status, and watch your productivity soar.</p>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      <footer id="about" className="border-t border-gray-100 py-12 text-center text-gray-500 text-sm">
        <p>(c) 2026 App. All rights reserved.</p>
        <div className="mt-4 flex justify-center gap-4">
          <a href="#" className="hover:text-black transition-colors">Privacy</a>
          <a href="#" className="hover:text-black transition-colors">Terms</a>
          <a href="#" className="hover:text-black transition-colors">Contact</a>
        </div>
      </footer>
    </main>
  );
}
