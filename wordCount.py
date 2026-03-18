#!/usr/bin/env python3
import sys
import os

def count_characters(file_path):
    """统计文件中的字符数"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return len(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)

def count_words(file_path):
    """统计文件中的单词数"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 用空格和逗号分割单词
        words = content.replace(',', ' ').split()
        return len(words)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)

def main():
    """主函数"""
    if len(sys.argv) != 3:
        print("Usage: wordCount.py -c/-w [input_file_name]")
        sys.exit(1)
    
    parameter = sys.argv[1]
    input_file = sys.argv[2]
    
    if parameter == '-c':
        count = count_characters(input_file)
        print(f"字符数：{count}")
    elif parameter == '-w':
        count = count_words(input_file)
        print(f"单词数：{count}")
    else:
        print("Invalid parameter. Use '-c' for character count or '-w' for word count.")
        sys.exit(1)

if __name__ == "__main__":
    main()
