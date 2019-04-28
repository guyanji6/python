import socket

eol1 = '\n\n\r'
eol2 = '\n\r'
body = '''hello,world <h1> frome Django </h1>'''

response_parames = [
    'http/1.0 200 OK',
    'data',
    body
]

response = '\r\n'.join(response_parames)

def handle_connnection(conn, addr) :
    request = ''

def main() :
    pass

if __name__ == '__main__' :
    main()