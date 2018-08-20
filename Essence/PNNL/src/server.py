#!/usr/bin/env python3

import http.server
import socketserver
import logging
import cgi

import sys


if len(sys.argv) > 2:
    PORT = int(sys.argv[2])
    I = sys.argv[1]
elif len(sys.argv) > 1:
    PORT = int(sys.argv[1])
    I = ""
else:
    PORT = 8080
    I = ""


class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.warning("======= GET STARTED =======")
        logging.warning(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.warning("======= POST STARTED =======")
        logging.warning(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        logging.warning("======= POST VALUES =======")
        for item in form.list:
            logging.warning(item)
        logging.warning("\n")
        http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = ServerHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Python http server (for testing purposes only)")
print("Serving at: http://%(interface)s:%(port)s" % dict(interface=I or "localhost", port=PORT))
httpd.serve_forever() # run forever
# httpd.handle_request()  # run once
