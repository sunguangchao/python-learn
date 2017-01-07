# -*- coding: utf-8 -*-

#author: guangchaosun


import re
import os

def get_files(path):
    filepath = os.listdir(path)
    files = []
    for fp in filepath:
        fppath = path + '/' + fp
        if(os.path.isfile(fppath)):
            files.append(fppath)
            tmp = fppath[2:]
            a = tmp[-2:]
            if(a == '.c' or a == '.h'):
                if os.system("clang-format -i " + tmp) == 0:
                    print tmp + ' has been format successfully'
                else:
                    print tmp + 'format failed'
        elif(os.path.isdir(fppath)):
            files += get_files(fppath)
    return files
    
if __name__ == '__main__':
    get_files('.')
