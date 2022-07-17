from http.server import BaseHTTPRequestHandler, HTTPServer

data = [1, 2, 3]
str_data = ",".join(map(str, data))


class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(str_data.encode())


def main():
    PORT = 8000
    server = HTTPServer(("", PORT), echoHandler)
    print(f"server running on {PORT}")
    server.serve_forever()


main()
