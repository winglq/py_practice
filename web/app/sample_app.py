#! /usr/bin/env python

# Python's bundled WSGI server
import app_db


def application(environ, start_response):
    # Sorting and stringifying the environment key, value pairs
    p = app_db.session.query(app_db.Person).all()
    print p
    response_body = '''
<html>
<title>All Customers</title>
<body>
<table><th><tr><td>id</td><td>name</td></tr></th>
<tr><td>%s</td><td>%s</td><td>%s</td></tr>
<tr><td>%s</td><td>%s</td><td>%s</td></tr>
</table>
</body>
</html>
''' % (p[0].id, str(p[0].name), str(p[0].address[0].email),
       p[1].id, str(p[1].name), str(p[1].address[0].email))
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]
