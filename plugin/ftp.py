#coding:utf-8

from framework import *


class Fuzz(FuzzBaseClass):
    def __init__(self):
        FuzzBaseClass.__init__(self)

    def FuzzStart(self,fuzz_info):
        s_initialize("user")
        s_string("USER")
        s_delim(" ")
        s_string(fuzz_info['user'].encode('ascii'))
        s_static("\r\n")

        s_initialize("pass")
        s_string("PASS")
        s_delim(" ")
        s_string(fuzz_info['pass'].encode('ascii'))
        s_static("\r\n")

        s_initialize("stor")
        s_string("STOR")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        s_initialize("retr")
        s_string("RETR")
        s_delim(" ")
        s_string("AAAA")
        s_static("\r\n")

        self.session_.connect(s_get("user"))
        self.session_.connect(s_get("user"), s_get("pass"))
        self.session_.connect(s_get("pass"), s_get("stor"))
        self.session_.connect(s_get("pass"), s_get("retr"))
