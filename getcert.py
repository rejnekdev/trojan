# author discord ; rejnekᴅᴇᴠ#3246

import socket
import ssl
import sys

def input_with_default(prompt, default):
    print('{} [{}]: '.format(prompt, default), file=sys.stderr, end='')
    line = input()
    return line if line else default

def main(argc, argv):
    if argc == 1:
        hostname = input_with_default('Enter hostname', 'example.com')
        port = int(input_with_default('Enter port number', '443'))
    elif argc == 2:
        hostname = argv[1]
        port = 443
    elif argc == 3:
        hostname = argv[1]
        port = int(argv[2])
    else:
        print('usage: {} [hostname] [port]'.format(argv[0]), file=sys.stderr)
        exit(1)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    with socket.create_connection((hostname, port)) as sock:
        with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
            print(ssl.DER_cert_to_PEM_cert(ssock.getpeercert(True)), end='')

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
