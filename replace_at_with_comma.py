import requests
import re

def replace_at_symbol():
    # 从URL获取内容
    url = "https://pastebin.com/raw/V0BhYHF4"
    response = requests.get(url)
    content = response.text
    
    # 替换所有@为,
    modified_content = content.replace('@', ',')
    
    # 保存到文件
    with open('modified_file.txt', 'w') as f:
        f.write(modified_content)
    
    print("替换完成，结果已保存到modified_file.txt")

if __name__ == "__main__":
    replace_at_symbol()
