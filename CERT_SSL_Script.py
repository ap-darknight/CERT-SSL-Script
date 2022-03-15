import socket
import ssl
import datetime

hostname = 'www.python.org'
port = 443
context = ssl.create_default_context()
current_date = datetime.datetime.now()
formatted_date = current_date.strftime('%b %d %H:%M:%S %Y %Z')
 
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert_expiry = ssock.getpeercert()['notAfter']
        cert_exp_date = datetime.datetime.strptime(cert_expiry, '%b %d %H:%M:%S %Y %Z')
        print(cert_exp_date - current_date)
        print(formatted_date, cert_expiry)


