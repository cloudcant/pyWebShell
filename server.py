import socketserver
import logging

logging.basicConfig(level=logging.INFO)

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        logging.info(f"Received connection from {self.client_address[0]}")
        
        # Read the HTML file
        with open('index.html', 'r') as f:
            html = f.read()
        
        self.request.sendall(b"HTTP/1.1 200 OK\n")
        self.request.sendall(b"Content-Type: text/html\n\n")
        
        self.request.sendall(html.encode())

# def server to server start
server = socketserver.TCPServer(('localhost', 8000), MyTCPHandler)

# server start
server.serve_forever()
