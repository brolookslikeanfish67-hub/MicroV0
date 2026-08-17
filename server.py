import http.server
import socketserver
import threading
import json
from config import BASE_TEMPLATE

class PreviewServer:
    def __init__(self, port=8080):
        self.port = port
        self.version = 0
        initial_placeholder = "<div class='p-12 text-center text-slate-400'>✨ Awaiting your first AI component generation prompt...</div>"
        self.current_html = BASE_TEMPLATE.format(COMPONENT_CODE=initial_placeholder)
        
    def update_canvas(self, raw_component_code):
        """Increments version registry and re-injects raw client-side blocks."""
        self.version += 1
        self.current_html = BASE_TEMPLATE.format(COMPONENT_CODE=raw_component_code)

    def start(self):
        """Launches the lightweight HTTP server in a separate thread context."""
        canvas_context = self
        
        class DynamicHandler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/':
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(canvas_context.current_html.encode('utf-8'))
                elif self.path == '/version':
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"version": canvas_context.version}).encode('utf-8'))
                else:
                    self.send_error(404)

            def log_message(self, format, *args):
                return # Mute console outputs to preserve a clean terminal UI

        server = socketserver.TCPServer(("", self.port), DynamicHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        print(f"🌐 MicroV0 Live Canvas running natively at: http://localhost:{self.port}")
