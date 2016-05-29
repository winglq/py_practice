#! /usr/bin/env python

# Python's bundled WSGI server
from wsgiref.simple_server import make_server
from app.sample_app import application

# Instantiate the server
httpd = make_server (
    '10.0.2.15', # The host name
    8080, # A port number where to wait for the request
    application # The application object name, in this case a function
    )
# Wait for a single request, serve it and quit
httpd.handle_request()
