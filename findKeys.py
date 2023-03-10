#使用示例：
# python findKeys.py -s D:\sourceCode\jeecg-boot-3.4.4 -k upload
# python findKeys.py -s D:\sourceCode\jeecg-boot-3.4.4 -f D:\sourceCode\sink.txt

import os
import re
import argparse

def search_string_in_files_in_folder(folder_path, keywords):
    # 获取文件夹中所有文件的文件名
    file_names = os.listdir(folder_path)

    # 遍历每个文件
    for file_name in file_names:
        # 拼接文件路径
        file_path = os.path.join(folder_path, file_name)

        # 判断该文件是否是文件夹
        if os.path.isdir(file_path):
            # 如果是文件夹则递归调用该函数
            search_string_in_files_in_folder(file_path, keywords)
        else:
            try:
            # 打开文件并读取内容
                if(file_path.endswith(".java")):
                    with open(file_path, 'r',encoding='utf-8') as file:
                        file_content = file.read()

                # 搜索文件内容中是否存在指定字符串
                        for keyword in keywords:
                            if re.search(keyword, file_content):
                            # 如果存在则输出文件名
                                print(keyword+": "+file_path)

                # 关闭文件
                    file.close()
            except:
                continue

args = argparse.ArgumentParser()
args.add_argument('-s', '--source', type=str, required=True,help='源码目录')
args.add_argument('-k', '--key', type=str, help='关键字')
args.add_argument('-f', '--file', type=str, help='关键字路径')
parse_args = args.parse_args()

keywords = []

if(parse_args.key):
    print(parse_args.key)
    keywords.append(parse_args.key)

else:
    with open(parse_args.file, 'r', encoding='utf-8') as file:
       key = file.readline()
       while(key):
           key = key.strip()
           key = key.strip("\n")
           keywords.append(key)
           key = file.readline()
    file.close()

search_string_in_files_in_folder(parse_args.source, keywords)
