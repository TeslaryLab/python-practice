import socket, ssl
# import pprint

def parsed_url(url):
    '''
    url 可能的值如下
    g.cn
    g.cn/
    g.cn:3000
    g.cn:3000/search
    http://g.cn
    https://g.cn
    http://g.cn/

    NOTE:
    没有 protocol 时, 默认协议是 http

    在 http 下 默认端口是 80
    在 https 下 默认端口是 443
    :return : tuple, 内容如下 (protocol, host, port, path)
    '''
    host = ''
    port = ''
    # 提取协议
    if url.find("://") == -1:
        protocol = 'http'
        host_str = url
    else:
        url_list = url.split("://")
        protocol = url_list[0]
        host_str = url_list[1]

    # 提取域名
    port_and_path = ''
    flag = True
    for char in host_str:
        # 遇到:或/就进入port和path的提取模式
        if flag and char != ':' and char != '/':
            host = host + char
        else:
            flag = False
            port_and_path = port_and_path + char

    # 提取port和path
    length = port_and_path.__len__()
    if '' != port_and_path and ':' == port_and_path[0]:
        if port_and_path.find("/") != -1:
            foo_list = port_and_path[1:length].split("/")
            port = foo_list[0]
            path = foo_list[1]
        else:
            port = port_and_path[1:length]
            path = ''
    else:
        path = port_and_path[1:length]

    # 检查与填充
    if '' == port:
        if 'http' == protocol:
            port = '80'
        else:
            port = '443'

    if '' == path:
        path = '/'
    else:
        path = '/' + path

    port = int(port)
    protocol = protocol.upper()
    return protocol, host, port, path


def get(url):
    '''
    返回的数据类型为 bytes
    '''
    (protocol, host, url_port, path) = parsed_url(url)
    context = ssl.create_default_context()
    context.check_hostname = True
    conn = socket.socket(socket.AF_INET)
    if protocol == 'HTTPS':
        conn = context.wrap_socket(conn, server_hostname=host)
        # cert = conn.getpeercert()
        # pprint.pprint(cert)
    
    conn.connect((host, url_port))
        
    http_request = 'GET {} HTTP/1.1\r\nhost:{}\r\nConnection: close\r\n\r\n'.format(path, host)
    request = http_request.encode('utf-8')
    conn.send(request)
    response = b''
    response_header = conn.recv(1024)
    # get stauts
    status = str(response_header).split("\r\n")[0].split(" ")[1]
    print('status,', status)
    response += response_header
    while True:
        r = conn.recv(1024)
        response += r
        if len(r) == 0:
            break
    return response

"""
在 Python3 中，bytes 和 str 的互相转换方式是
str.encode('utf-8')
bytes.decode('utf-8')
send 函数的参数和 recv 函数的返回值都是 bytes 类型
"""

if __name__ == '__main__':
    url = 'https://movie.douban.com/top250'
    r = get(url)
    with open('data.html', 'w+', encoding='utf-8') as f:
        f.write(str(r,encoding='utf-8'))
