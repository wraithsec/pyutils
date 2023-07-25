#!/usr/bin/env python3
import argparse
import http.server
import ssl

def main(args: list) -> None:
    # Define the server address and port
    server_address = (args.i, args.p)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)


    # Create an SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    try:
        context.load_cert_chain(certfile=args.c, keyfile=args.k)
    except FileNotFoundError:
        print(f'[-] Cert files {args.c} and {args.k} don\'t exist!')
        exit(1)

    delim='---------------'
    print('[ ] Serving your https server! Ctrl+C to stop.')
    print('[ ] Use either of the following command examples to grab files:')
    print(delim*2)
    print(f'ncat --ssl {args.i} {args.p} > outfile\n\nGET /file HTTP/1.1\nHost: {args.i}\n')
    print(delim*2)
    print(f'curl -vv -k https://{args.i}:{args.p}/file -o outfile')
    print(delim*2)
    print(f'wget --no-check-certificate https://{args.i}:{args.p}/file -O outfile')
    print(delim*2)
    print('\n','\n')

    # Wrap the HTTP server in an SSL context and serve
    try:
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        httpd.serve_forever()
    except Exception as e:
        print(f"Exceptino encountered trying to serve the wrapped server: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-p', type=int, help='Port to serve on.', default=8443)
    parser.add_argument('-i', type=str, help='Ip to serve on.', default='0.0.0.0')
    parser.add_argument('-k', type=str, help='Server key.', default='server.key')
    parser.add_argument('-c', type=str, help='Server cert.', default='server.crt')
    args = parser.parse_args()
    main(args)
