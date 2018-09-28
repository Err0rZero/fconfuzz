#coding:utf-8

from framework import *


class Fuzz(FuzzBaseClass):
    def __init__(self):
        FuzzBaseClass.__init__(self)

    def FuzzStart(self,fuzz_info):
        self.host_ = fuzz_info['host']
        self.port_ = fuzz_info['port']
        self.proto_ = fuzz_info['proto']

        init_name = "FUZZHTTP"
        s_initialize(init_name)
        with s_block("Request-Line"):
            s_group("Method", ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE'])
            s_delim(" ", name='space-1')
            s_string("/dvwa/login.php", name='Request-URI')
            s_delim(" ", name='space-2')
            s_string('HTTP/1.1', name='HTTP-Version')
            s_static("\r\n", name="Request-Line-CRLF")
            s_string("Host")
            s_delim(":")
            s_delim(" ")
            s_string(self.host_)
            s_delim("\r\n")

            s_static("Accept: ")
            s_string("image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, application/x-silverlight, application/x-shockwave-flash, */* ", name="ACCEPT")
            s_static("\r\n")

            s_static("User-Agent: ")
            s_string("Mozilla/5.0 (Windows; U)",name="UA")
            s_static("\r\n")

            s_static("Accept-Language: ")
            s_string("en-us",name="AL")
            s_delim(",")
            s_string("en;q=0.5")
            s_static("\r\n")

            s_static("Keep-Alive: ")
            s_string("300",name="KA")
            s_static("\r\n")

            s_static("Connection: ")
            s_string("keep-alive",name="CNN")
            s_static("\r\n")

            s_static("Referer: ")
            s_string(self.host_,name="RF")
            s_static("\r\n")

            s_static("Cookie: ")
            s_string("auth",name="COOKIE")
            s_delim("=")
            s_string("1234567890")
            s_static("\r\n")

            s_static("Cache-Control: ")
            s_string("no-cache",name="CCCC")
            s_static("\r\n")

            s_static("Accept-Encoding: ")
            s_string("gzip, deflate",name="AEEEE")
            s_static("\r\n")



        s_static("\r\n", "Request-CRLF")
        self.session_.connect(s_get(init_name))