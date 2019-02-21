# xml两种解析方式sax和dom
# dom生成整个结点树，占内存，sax边读边解析，需要自己处理事件
# sax事件主要为start_element，end_element 和 char_data
from xml.parsers.expat import ParserCreate


class MyHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element:%s,attrs:%s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element:%s' % (name))

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
 <li><a href="/python">Python</a></li>
 <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = MyHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler  = handler.char_data
parser.Parse(xml)
