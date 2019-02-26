# 参数1：dict类型，request信息 参数2：发送response的函数
def hello_wsgi(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>hello,wsgi!<h1>']
