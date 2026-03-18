# Word Count Tool

## 功能说明

一个命令行工具，用于统计文本文件的字符数或单词数。

## 用法

```bash
python3 wordCount.py [parameter] [input_file_name]
```

### 参数说明
- `-c`：统计字符数（包括空格、水平制表符、换行符）
- `-w`：统计单词数（由空格或逗号分割的视为单词，不做有效性校验）

### 示例

```bash
# 统计 input.txt 中的字符数
python3 wordCount.py -c input.txt

# 统计 input.txt 中的单词数
python3 wordCount.py -w input.txt
```

## 输出格式

- 字符数：n
- 单词数：n

其中 n 为统计的字符数或单词数。
