#!/usr/bin/env python
# -*- coding=utf-8 -*-
# coding: utf-8
 
import os
import shutil
 
 
def show_files(path):
    # 遍历当前目录下所有文件及文件夹
    file_list = os.listdir(path)
 
    # 循环判断file_list中每个元素是文件还是文件夹,若是文件，传入list，若是文件夹，再递归
    for file in file_list:
 
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
 
        # 判断是否是文件夹，若是重新递归
        if os.path.isdir(cur_path):
            show_files(cur_path)
        else:
            """
            给每个文件重新修改后缀
            """
            new_suf = cur_path.replace('.html', '.doc')
            print(new_suf)
 
            # 改完后缀后，需要移动并覆盖源文件
            shutil.move(cur_path, new_suf)
 
 
show_files('D:\\ns3_result\\test\\')
