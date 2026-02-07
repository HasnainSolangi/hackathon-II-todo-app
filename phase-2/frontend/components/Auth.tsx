"use client";
import { useMemo, useState } from 'react';
import Image from 'next/image';
import { authClient } from "@/lib/auth-client";
import { Github, ArrowRight } from 'lucide-react';

export default function Auth() {
    const [isLogin, setIsLogin] = useState(true);
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
    const [loading, setLoading] = useState(false);

    const validationError = useMemo(() => {
        if (!email.trim()) return "Email is required";
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return "Enter a valid email";
        if (!password.trim()) return "Password is required";
        if (password.length < 8) return "Password must be at least 8 characters";
        if (!isLogin && !name.trim()) return "Full name is required";
        return null;
    }, [email, password, name, isLogin]);

    const handleAuth = async () => {
        if (validationError) {
            return;
        }
        setLoading(true);
        try {
            if (isLogin) {
                await authClient.signIn.email({
                    email,
                    password,
                    callbackURL: "/"
                }, {
                    onSuccess: async () => {
                        window.location.reload();
                    },
                    onError: (ctx) => {
                        alert(ctx.error.message);
                        setLoading(false);
                    }
                });
            } else {
                await authClient.signUp.email({
                    email,
                    password,
                    name,
                    callbackURL: "/"
                }, {
                    onSuccess: async () => {
                        window.location.reload();
                    },
                    onError: (ctx) => {
                        alert(ctx.error.message);
                        setLoading(false);
                    }
                });
            }
        } catch (error) {
            setLoading(false);
            console.error(error);
        }
    };

    const handleSocial = async (provider: 'github' | 'google') => {
        setLoading(true);
        await authClient.signIn.social({
            provider,
            callbackURL: "/"
        }, {
            onSuccess: async () => {
                // Redirect handled by callbackURL, but we can ensure reload if needed
                window.location.href = "/";
            },
            onError: (ctx) => {
                alert(ctx.error.message);
                setLoading(false);
            }
        });
    };

    return (
        <div className="w-full max-w-md mx-auto p-8 rounded-2xl bg-white dark:bg-gray-800 shadow-xl border border-gray-100 dark:border-gray-700">
            <div className="text-center mb-8">
                <h2 className="text-3xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-2">
                    {isLogin ? 'Welcome Back' : 'Create Account'}
                </h2>
                <p className="text-gray-500 dark:text-gray-400 text-sm">
                    {isLogin ? 'Enter your details to access your tasks' : 'Start your productivity journey today'}
                </p>
            </div>

            <div className="flex flex-col gap-4 mb-6">
                {!isLogin && (
                    <div className="relative">
                        <input
                            type="text"
                            placeholder="Full Name"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            className="w-full p-3 pl-4 bg-gray-50 dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all text-black dark:text-white placeholder:text-gray-400 dark:placeholder:text-gray-500"
                        />
                    </div>
                )}
                <input
                    type="email"
                    placeholder="Email Address"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="w-full p-3 pl-4 bg-gray-50 dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all text-black dark:text-white placeholder:text-gray-400 dark:placeholder:text-gray-500"
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full p-3 pl-4 bg-gray-50 dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all text-black dark:text-white placeholder:text-gray-400 dark:placeholder:text-gray-500"
                />
            </div>

            <button
                onClick={handleAuth}
                disabled={loading || !!validationError}
                className="w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white p-3 rounded-xl font-semibold hover:opacity-90 transition-all flex items-center justify-center gap-2 shadow-lg shadow-blue-500/30 disabled:opacity-50"
            >
                {loading ? 'Processing...' : (isLogin ? 'Sign In' : 'Sign Up')}
                {!loading && <ArrowRight size={18} />}
            </button>
            {validationError && (
                <p className="mt-2 text-sm text-red-500 text-center">{validationError}</p>
            )}

            <div className="relative my-6">
                <div className="absolute inset-0 flex items-center">
                    <div className="w-full border-t border-gray-200 dark:border-gray-700"></div>
                </div>
                <div className="relative flex justify-center text-sm">
                    <span className="px-2 bg-white dark:bg-gray-800 text-gray-400 dark:text-gray-500">Or continue with</span>
                </div>
            </div>

            <div className="grid grid-cols-2 gap-3 mb-6">
                <button
                    onClick={() => handleSocial('google')}
                    disabled={loading}
                    className="flex items-center justify-center gap-2 p-3 border border-gray-200 dark:border-gray-700 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition-all text-gray-700 dark:text-gray-300 font-medium disabled:opacity-50"
                >
                    <Image
                        src={isLogin ? "/google_sign_in_neutral.png" : "/google_sign_up_neutral.png"}
                        alt={isLogin ? "Sign in with Google" : "Sign up with Google"}
                        width={120}
                        height={36}
                        className="h-5 w-auto"
                    />
                </button>
                <button
                    onClick={() => handleSocial('github')}
                    disabled={loading}
                    className="flex items-center justify-center gap-2 p-3 border border-gray-200 dark:border-gray-700 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition-all text-gray-700 dark:text-gray-300 font-medium disabled:opacity-50"
                >
                    <Github size={20} />
                    GitHub
                </button>
            </div>

            <div className="text-center">
                <button
                    onClick={() => setIsLogin(!isLogin)}
                    className="text-sm text-gray-500 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                >
                    {isLogin ? "Don't have an account? Sign up" : "Already have an account? Sign in"}
                </button>
            </div>
        </div>
    );
}
