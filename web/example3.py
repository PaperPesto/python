from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET path", self.path)

        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, world! Welcome to root')
        if self.path == "/home":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, world! Welcome to home')
        if self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><head><title>Title goes here.</title></head>")
            self.wfile.write(b"<body><p>This is a test.</p>")
            a = "<p>You accessed path: %s</p>" % (self.path)
            self.wfile.write(a.encode())
            self.wfile.write(b"</body></html>")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
