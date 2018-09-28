#coding:utf-8


from boofuzz import *
from pyZZUF.pyZZUF import *


class FuzzBaseClass():
    def __init__(self):
        self.host_ = ""
        self.port_ = 0
        self.proto_ = ""
        self.session_ = None


    def __setSession__(self):
        connection = SocketConnection(self.host_, self.port_, proto=self.proto_)
        target = Target(connection=connection)
        self.session_ = Session(target=target)



    def FuzzStart(self,fuzz_info = {}):
        raise NotImplementedError


    def Run(self,fuzz_info):
        self.host_ = fuzz_info['host']
        self.port_ = fuzz_info['port']
        self.proto_ = fuzz_info['proto']
        self.__setSession__()

        self.FuzzStart(fuzz_info)
        self.session_.fuzz()


