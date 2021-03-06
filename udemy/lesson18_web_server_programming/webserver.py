# used to aasign the port number from the command line
import sys
import http.server

Handler = http.server.SimpleHTTPRequestHandler
Server = http.server.HTTPServer
Protocol = "HTTP/2.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

server_address = ('127.0.0.1', port)

Handler.protocol_version = Protocol
httpd = Server(server_address, Handler)

print("Serving HTTP")
httpd.serve_forever()