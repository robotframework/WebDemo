#!/usr/bin/env python

"""Simple HTTP server for Robot Framework web testing demo.

Usage:  server.py [port]

This server serves HTML pages under `html` directory. Server is started simply
by running this script from the command line or double-clicking it in file
manager. In the former case the server can be closed using Ctrl-C and in the
latter case by closing the opened window.

By default the server uses port 7272, but a custom port can be given as
an argument from the command line.
"""

from os import chdir
from os.path import abspath, dirname, join
from SocketServer import TCPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


ROOT = join(dirname(abspath(__file__)), 'html')
PORT = 7272


class RequestHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        self.do_GET()


def start_server(port=PORT):
    httpd = TCPServer(('localhost', int(port)), RequestHandler)
    chdir(ROOT)
    print 'Demo application starting on port %s.' % port
    httpd.serve_forever()


if __name__ == '__main__':
    import sys
    try:
        start_server(*sys.argv[1:])
    except (TypeError, ValueError):
        print __doc__
