import socket
import ssl
import datetime

hostname = 'www.python.org'
port = 443
context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.getpeercert()['notAfter'])
        print(datetime.datetime.now())
print(context)