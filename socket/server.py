import socket

host = '' # host为表示可以接受任何网络的连接
port = 2000

s = socket.socket()
s.bind((host,port)) # 1024以上自由绑定

def read_from_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

while True:
    backlog = 5
    s.listen(backlog) # 监听请求的数量
    connection, address = s.accept() 

    request = connection.recv(1024)
    request = request.decode('utf-8')
    # print('ip and resquest, {}\n{}\n'.format(address, request)) 
    # chrome发送空请求 导致页面crash
    line = request.split('\n')[0]
    print('line', line)
    path = line.split()[1]
    print('path, ', path)
    if path == '/pic':
        response = b'HTTP/1.1 200 OK\r\nContent-Type: text\html\r\n\r\n<h1>hello,world</h1><img src="/pic.jpg">'
    elif path == '/pic.jpg':
        response = b'HTTP/1.1 200 OK\r\nContent-Type: image\jpeg\r\n\r\n' + read_from_file('../tool/pic.jpg')
    else:
        response = b'HTTP/1.1 404 NOT FOUND\r\nContent-Type: text\html\r\n\r\n'
    connection.sendall(response)

    connection.close()
