#coding:utf-8

import os
import sys
import json
import time
from tty_menu import tty_menu

from celerycore.init import app


def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        file_name = dir.split("/")[-1]
        if file_name[-3:] == ".py" and file_name != "__init__.py":
            fileList.append(file_name[:-3])

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)

    return fileList


@app.task
def StartFuzz(funClass,load_dict):
    funClass.Run(load_dict)



if __name__ == "__main__":
    
    import_file_list = GetFileList('./plugin/',[])
    pos = tty_menu(import_file_list, "select fuzz plugin?")
    print("Your select is %s" % (import_file_list[pos]))

    import_str = "from plugin.%s import *" % import_file_list[pos]
    try:
        exec(import_str)
    except Exception as e:
        print(e)
        sys.exit("error: Main Job Error!")

    is_celery = False

    if len(sys.argv) >= 2:
        config_name = sys.argv[1]
        is_celery = True
    else:
        config_name = "default"


    with open("./configs/%s.json" % config_name, "r") as load_f:
        load_dict = json.load(load_f)

    load_dict =dict(load_dict)

    print("fuzz start...\r\n")
    time.sleep(2)

    fuzzing = Fuzz()
    #fuzzing.Run(load_dict)
    if is_celery:
        StartFuzz.apply_async((fuzzing, load_dict))
    else:
        fuzzing.Run(load_dict)


    #f = Fuzz()
    #f.Run({"host": "waftest.enmonster.com", "port": 80, "proto": "tcp"})