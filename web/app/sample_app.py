#! /usr/bin/env python

# Python's bundled WSGI server

def application (environ, start_response):
    # Sorting and stringifying the environment key, value pairs
    response_body = 'Hello World'
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

