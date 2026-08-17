#  MicroV0: The Minimalist Local Open-Source Alternative to Vercel v0

A modular, zero-dependency local engine that converts natural language prompts into production-ready Tailwind/HTML components with an automated browser live-reload loop. No monthly SaaS fees. No token walls.

## 🛠️ Architecture
- `app.py`: Interactive CLI shell runner.
- `engine.py`: Raw LLM prompt-engineering layout sanitizer.
- `server.py`: Multi-threaded local preview HTTP server.
- `config.py`: Central app themes and Tailwind layout scaffold.

##  Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/brolookslikeanfish67-hub/MicroV0
   cd MicroV0
   ```

2. **Install core dependencies:**
   ```bash
   pip install google-generativeai
   ```

3. **Provide your free API credential:**
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

4. **Boot the workspace sandbox:**
   ```bash
   python app.py
   ```
