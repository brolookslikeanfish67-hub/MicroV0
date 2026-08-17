import sys
import webbrowser
from config import API_KEY
from server import PreviewServer
from engine import GenerationEngine

def run_cli():
    if not API_KEY:
        print(" System Error: GEMINI_API_KEY environment variable is missing.")
        print(" Resolve by running: export GEMINI_API_KEY='your_key_here'")
        sys.exit(1)

    # Initialize detached modules
    server = PreviewServer(port=8080)
    server.start()
    
    engine = GenerationEngine(api_key=API_KEY)
    
    # Automatically fire up browser window to display sandbox canvas
    webbrowser.open("http://localhost:8080")

    print("\n Welcome to MicroV0: Open-Source In-Browser Component Builder")
    print("=========================================================================")
    print("Type out components or UI elements. Type 'exit' to terminate environment.")

    while True:
        try:
            prompt = input("\n UI Concept / Prompt: ").strip()
            if not prompt or prompt.lower() == 'exit':
                break

            print(" Architecting layouts, rendering CSS components...")
            component_code = engine.generate_component(prompt)
            
            # Hot reload gets dispatched automatically via state tracking
            server.update_canvas(component_code)
            print(" Hot-swap update pushed down runtime. Check your canvas window!")

        except KeyboardInterrupt:
            break

    print("\n MicroV0 local execution context safely terminated.")

if __name__ == "__main__":
    run_cli()
