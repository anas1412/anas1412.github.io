from livereload import Server, shell
import http.server
import socketserver
import threading

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='.', **kwargs)

# Function to run the HTTP server
def run_http_server():
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        print(f'Serving HTTP on port {PORT}...')
        httpd.serve_forever()

# Start the HTTP server in a separate thread
http_thread = threading.Thread(target=run_http_server)
http_thread.daemon = True
http_thread.start()

# Use livereload to watch for changes and refresh
server = Server()

# Watch HTML, CSS, and JS files for changes
server.watch('*.html')
server.watch('assets/css/*.css')
server.watch('*.js') # Watching root JS files like posts.js
server.watch('assets/js/*.js') # Watching JS files in assets/js if any

print(f'LiveReload server starting on http://localhost:{PORT}')
print('Open your browser to this address.')
# Serve on a different port for livereload websocket if needed, or use default
server.serve(port=35729, host='localhost', root='.')