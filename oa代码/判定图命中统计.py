#!/usr/bin/env python

# _*_ coding:utf-8 _*_

'''

@author: diw

@contact: di.W@hotmail.com

@file: extract_fromxlsx.py

@time: 2018/7/12 13:35

@desc:从xlsx中提取所要的数据

'''
import os
import xlrd
import xlwt
import sys

def xlsxTransformer(filepath):
    print('标签计数ing')
    for keyword in keyword_dic.keys():
        result = 0
        workbook = xlrd.open_workbook(filepath)
        sheetList = workbook.sheet_names()
        # print(sheetList)
        sheet_name = workbook.sheet_names()[1]
        # print(sheet_name)
        sheet = workbook.sheet_by_name(sheet_name)
        colnum = sheet.ncols
        row = sheet.nrows
        # print(colnum)
        # print(row)
        for i in range(1,row):
            # print('第一行' + str(i))
            row_data = sheet.row_values(i)
            # print(row_data)
            for j in range(0,6):
                # print(j)
                if(row_data[j].strip() == keyword):
                    result += row_data[6]
                    break
        keyword_dic[keyword] = result
    # for sheetName in sheetList:
    #     print("-------子表："+sheetName+"------")
    #     table=data.sheet_by_name(sheetName)
    #     for colnum in range(table.ncols):
    #         for rownum in range(1,table.nrows):
    #             #if(table.cell(rownum,colnum)):
    #             print(table.cell(rownum,colnum))

def get_allkeyword(filepath):
    print('标签抽取')
    workbook = xlrd.open_workbook(filepath)
    sheetList = workbook.sheet_names()
    # print(sheetList)
    sheet_name = workbook.sheet_names()[1]
    # print(sheet_name)
    sheet = workbook.sheet_by_name(sheet_name)
    colnum = sheet.ncols
    row = sheet.nrows
    for i in range(1, row):
        row_data = sheet.row_values(i)
        for j in range(0, 6):
            if(row_data[j].strip() == ''):
                continue
            if(row_data[j].strip() not in keyword_dic.keys()):
                keyword_dic[row_data[j]] = 0

def outputtofile(wt_filepath):
    print('文件输出ing')
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('统计结果')
    keyword_num = len(keyword_sorted)
    for i in range(0,keyword_num):
        worksheet.write(i, 0, label = keyword_sorted[i][0])
        worksheet.write(i, 1, label = keyword_sorted[i][1])
    workbook.save(wt_filepath)
if __name__ == '__main__':
    keyword_dic = {}
    temp = 0
    filepath = input('请拖拽判定图初步统计表excel文件至cmd窗口\n')
    filepath = filepath.replace('\\', '/').replace('"','').strip()
    wt_filepath = "/Users/diw/Desktop/判定图标引_统计输出.xls"
    while(os.path.exists(wt_filepath)):
        temp += 1
        wt_filepath = "/Users/diw/Desktop/判定图标引_统计输出" + str(temp) + ".xls"


    get_allkeyword(filepath)
    xlsxTransformer(filepath)
    for key,keyvalue in keyword_dic.items():
        print(key+ ':' + str(keyvalue))

    keyword_sorted = sorted(keyword_dic.items(), key=lambda x: x[1], reverse=True)
    # print(keyword_sorted)
    outputtofile(wt_filepath)
    count = 0
    for key,result in keyword_dic.items():
        count+=result
    print(count)