# _*_ coding:utf-8 _*_

'''

@author: MenghanSun

@contact: smh_gabriella@buaa.edu.cn

@file: xlsx_tranformer.py

@time: 2018/7/12 14:27

@desc:

'''

import xlrd
import sys

def xlsxTransformer(filepath):
    data = xlrd.open_workbook(filepath)
    sheetList = data.sheet_names()
    #print(sheetList)
    for sheetName in sheetList:
        print("============子表："+sheetName+"============")
        table=data.sheet_by_name(sheetName)
        for colnum in range(table.ncols):
            print("---"+table.row(0)[colnum].value+"---")
            textList=[]
            for rownum in range(1,table.nrows):
                text=str(table.cell(rownum,colnum)).strip()
                if(text!="empty:''"):
                    textList.append(text.replace("text:","").replace("'",""))
            print(','.join(textList))
        print("\n")


if __name__ == '__main__':
    #excel文件路径
    filepath = input('请拖拽待处理excel文件至cmd窗口\n')
    filepath = filepath.replace('\\','/').replace('"','').strip()
    # print(filepath)
    xlsxTransformer(filepath)