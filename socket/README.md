# server client

using socket to catch http data.

http data structs:

1. 请求行和响应行
2. Header(Host必选, 另外有一个字段带有\r\n)
3. \r\n
4. body(可选)

