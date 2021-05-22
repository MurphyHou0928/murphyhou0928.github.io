# 关于项目

## 起因

- 个人网页在开发过程中遇到了一些问题，在做照片墙的时候，因为需要导入大量的图片素材，因此需要对图片进行批量的重命名操作，其实Windows有自己的批量重命名功能，这个功能之前也是频繁使用。但是最近在写markdown文件的时候遇到了一些问题：
- markdown文件中插入图片的时，Windows的这种重命名方法就会与markdown的语法冲突，因为Windows上的重命名时，文件的名称格式是：test (1).jpg，正是这个括号)的存在，让markdown语法产生了冲突，因此需要一个更好的重命名方法；
- 毫无疑问，python可以解决这种问题（对python就是这么**自信**）

## 资料查阅

- 网上一搜，果然有相关的代码，那就没有必要重复的造轮子了
- 我只需要参考相关关键部分的使用，并加上自己的修改，是的程序更符合我自己的使用需求

# 项目解析（正在修改代完善代码中）

- 导入库

  ``` python
  import os
  # os 顾名思义，就是与操作系统相关的标准库。如：文件，目录，执行系统命令等。
  import numpy as  np
  # NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。
  ```

- 

  ``` python
  
  ```

- 

  ``` python
  
  ```

- 

  ``` python
  
  ```

- 

  ``` python
  
  ```

- 

  ``` python
  
  ```

  

  ``` python
  
  ```

  

# 项目完整代码

``` python
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
```

- 程序结果

# 关于项目的思考

- 