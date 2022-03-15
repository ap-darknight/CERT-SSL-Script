import socket
import ssl
import datetime

hostnames = ['www.python.org']
port = 443
expire_limit = 3;

def generate_new_ssl(hostame, port):
    print("Hello");

def install_new_ssl(hostame, port):
    print("Hello---2");

def expiring_soon(hostname, port):
    context = ssl.create_default_context()
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime('%b %d %H:%M:%S %Y %Z')
    cert_exp_date = 0
    
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert_expiry = ssock.getpeercert()['notAfter']
            cert_exp_date = datetime.datetime.strptime(cert_expiry, '%b %d %H:%M:%S %Y %Z')
            print(cert_exp_date - current_date)
            print(formatted_date, cert_expiry)

    days_after = int((cert_exp_date - current_date).days);
    print(days_after)
    if(days_after <= expire_limit): return True
    return False

if __name__ == "__main__": 
    for host in hostnames:
        if(expiring_soon(host, port)):
            generate_new_ssl(host,port)
            install_new_ssl(host,port)
        else: print('Saved!!')

