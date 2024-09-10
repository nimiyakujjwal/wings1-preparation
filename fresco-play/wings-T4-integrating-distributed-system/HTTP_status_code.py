"""
HTTP Status Code - Fresco play problem

"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from unittest import result

class simpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/get":
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"GET request received")
        elif self.path == "/redirect":
            self.send_response(302)
            self.send_header("Location", "https://www.example.com")
            self.end_headers()
        elif self.path == "/divide_by_zero":
            result = 1 / 0
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.wfile.read(content_length)

        if self.path == "/post":
            if post_data.decode("utf-8") == "('username':user, 'password': 'pass')":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(b"POST request received with correct credential")
            else:
                self._send_response()
                self.send_header("content-types", "application/json")
                self.end_headers()

def run(server_class = HTTPServer, handler_class = simpleHTTPRequestHandler, port = 5000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting server on port {}...".format(port))
    httpd.serve_forever()

if __name__ == "__main__":
    run()
