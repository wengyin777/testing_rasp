import os
from http.server import HTTPServer, CGIHHTTPRequestHandler

os.chidr('.')

server_object = HTTPServer(server_address=('',80),RequestHandlerClass=CGIHTTPRequestHandler)

server_object.serve_forever()
