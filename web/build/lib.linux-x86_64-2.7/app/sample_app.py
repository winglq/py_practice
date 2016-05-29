#! /usr/bin/env python

# Python's bundled WSGI server
import app_db


def application(environ, start_response):
    # Sorting and stringifying the environment key, value pairs

    p = app_db.Person(id=1, name="Fake")
    response_body = 'Hello World %s' % p.name
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]
