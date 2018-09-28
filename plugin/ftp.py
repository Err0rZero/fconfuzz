#coding:utf-8

from framework import *


class Fuzz(FuzzBaseClass):
    def __init__(self):
        FuzzBaseClass.__init__(self)

    def FuzzStart(self,fuzz_info):
        s_initialize("user")
        s_static("USER")
        s_delim(" ")
        s_string(fuzz_info['user'].encode('ascii'))
        s_static("\r\n")

        s_initialize("pass")
        s_static("PASS")
        s_delim(" ")
        s_string(fuzz_info['pass'].encode('ascii'))
        s_static("\r\n")

        s_initialize("stor")
        s_static("STOR")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        s_initialize("retr")
        s_static("RETR")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        s_initialize("port")
        s_static("PORT")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        s_initialize("appe")
        s_static("APPE")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        s_initialize("dele")
        s_static("DELE")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        s_initialize("rest")
        s_static("REST")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        s_initialize("cwd")
        s_static("CWD")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        s_initialize("list")
        s_static("LIST")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        s_initialize("mkd")
        s_static("MKD")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        s_initialize("nlst")
        s_static("NLST")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        s_initialize("stat")
        s_static("STAT")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        self.session_.connect(s_get("user"))
        self.session_.connect(s_get("user"), s_get("pass"))
        self.session_.connect(s_get("pass"), s_get("stor"))
        self.session_.connect(s_get("pass"), s_get("retr"))
        self.session_.connect(s_get("pass"), s_get("port"))
        self.session_.connect(s_get("pass"), s_get("appe"))
        self.session_.connect(s_get("pass"), s_get("dele"))
        self.session_.connect(s_get("pass"), s_get("cwd"))
        self.session_.connect(s_get("pass"), s_get("list"))
        self.session_.connect(s_get("pass"), s_get("mkd"))
        self.session_.connect(s_get("pass"), s_get("nlst"))
        self.session_.connect(s_get("pass"), s_get("stat"))
