#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-07 11:18:07
# @Author  : di.W (di.W@hotmail.com)
# @Link    : ${link}
# @Version : $Id$

import xml.etree.cElementTree as ET
url = input('请拖动xml文件到窗口').replace('\\', '/')
# tree = ET.ElementTree(file=url)
filename_withpf = url.split('/')[-1]
print(filename_withpf)
# add_keyword
file_path = url.replace(filename_withpf,'panding_feaword.txt')
print(file_path)
# root = tree.getroot()
# feawords_list = []
# for elem in tree.iterfind('root/NewFeatureWords'):
#     for feaword in elem.attrib['feawords'].strip().split(','):
#         feawords_list.append(feaword.strip())
# # print(feawords_list)

# print('输出文件中')
# with open(file_path,'w+',encoding='utf-8') as f:
#     for fea in feawords_list:
#         f.write(fea.strip())
#         f.write('\n')
# print('输出成功')
