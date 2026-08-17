import os

# Ensure the system has access to the underlying LLM
API_KEY = os.getenv("GEMINI_API_KEY")

# HTML Scaffold with embedded Tailwind, Lucide Icons, and hot-reload polling script
BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MicroV0 Preview Canvas</title>
    <script src="https://tailwindcss.com"></script>
    <script src="https://unpkg.com"></script>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col items-center justify-center p-6">
    <div id="app-root" class="w-full max-w-5xl bg-slate-800 rounded-2xl shadow-2xl border border-slate-700/50 overflow-hidden">
        {COMPONENT_CODE}
    </div>
    <script>
        lucide.createIcons();
        
        // Lightweight polling mechanism to trigger instant browser reloads
        let currentVersion = null;
        setInterval(async () => {
            try {
                let res = await fetch('/version');
                let data = await res.json();
                if (currentVersion === null) currentVersion = data.version;
                if (currentVersion !== data.version) window.location.reload();
            } catch(e) {}
        }, 800);
    </script>
</body>
</html>"""

SYSTEM_INSTRUCTION = """
You are a senior frontend engineer outputting valid HTML and Tailwind CSS layout blocks.
Build fully responsive, premium, polished components. Use dark backgrounds to match the slate theme.
Incorporate Interactive JS logic within <script> tags for dynamic button clicks, tabs, or data adjustments if requested.
Return ONLY raw component markup. Do NOT wrap output inside markdown ```html blocks.
"""
