import http.server
import socket
import socketserver
import webbrowser
import pyqrcode

# Set the port for the server
PORT = 8010

# Function to get the server's IP address
def get_server_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

# Function to generate QR code
def generate_qr_code(ip_address, port):
    url = f"http://{ip_address}:{port}"
    qr = pyqrcode.create(url)
    qr.png("file_share_qr.png", scale=8)

# Function to start the HTTP server
def start_http_server(port):
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("Serving at port", port)
        print("Type this in your browser:", f"http://localhost:{port}")
        httpd.serve_forever()

if __name__ == "__main__":
    ip_address = get_server_ip()
    generate_qr_code(ip_address, PORT)
    webbrowser.open("file_share_qr.png")
    start_http_server(PORT)
