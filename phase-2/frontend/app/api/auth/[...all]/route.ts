import { auth } from "@/lib/auth"; // import your auth instance
import { toNextJsHandler } from "better-auth/next-js";

const handler = toNextJsHandler(auth);
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const MIN_PASSWORD_LENGTH = 8;

export const GET = handler.GET;
export const POST = async (req: Request) => {
    const cloned = req.clone();
    try {
        const body = await cloned.json();
        const email = typeof body?.email === "string" ? body.email.trim() : null;
        const password = typeof body?.password === "string" ? body.password : null;
        const name = typeof body?.name === "string" ? body.name.trim() : null;

        if (email && !EMAIL_RE.test(email)) {
            return Response.json({ error: "Invalid email format." }, { status: 400 });
        }

        if (password && password.length < MIN_PASSWORD_LENGTH) {
            return Response.json({ error: "Password must be at least 8 characters." }, { status: 400 });
        }

        if (name !== null && name.length === 0) {
            return Response.json({ error: "Full name is required." }, { status: 400 });
        }
    } catch {
        // If body isn't JSON, let Better Auth handle it.
    }

    return handler.POST(req);
};
