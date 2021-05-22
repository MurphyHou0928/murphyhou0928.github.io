# -*- coding : utf-8 -*-
# Time       : 2021/5/22 18:45
# Author     : MurphyHou
# Proj_Name  : rename
# File_Name  : rename.py
# Software   : PyCharm
# =======Here We Go!=======

import os
import numpy as  np
class BatchRename():
    '''
    批量重命名文件夹中的图片文件

    '''
    def __init__(self):

        path=input("请输入文件的地址:")

        self.path = [path]
    def rename(self):

        rename_style=input("请输入你需要的文件的重命名的前缀（例如：5_20_s）:")
        file_format=input("请输入你想要修改的文件的格式(例如：.jpg):")
        for j in range(1):
            filelist = os.listdir(self.path[j])
            total_num = len(filelist)
            print(total_num)
            i = 0
            for item in filelist:
                if item.endswith(file_format):
                    src = os.path.join(os.path.abspath(self.path[j]), item)
                    dst = os.path.join(os.path.abspath(self.path[j]), rename_style +str(i) + file_format)
                    try:
                        os.rename(src, dst)
                        print ('converting %s to %s ...' % (src, dst))
                        i = i + 1
                    except:
                        continue

            print ('total %d to rename & converted %d %s' % (total_num, i,file_format))
            # print('i = %d'%(i))

if __name__ == '__main__':
    print("该程序会把某一个路径下的所有的某一种文件格式重命名为相同类型的命名格式！")
    demo = BatchRename()
    demo.rename()