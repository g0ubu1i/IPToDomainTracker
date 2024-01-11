import requests
import re
from colorama import Fore
from tabulate import tabulate
from core import find
import argparse


def find_domain(text, ip):
    # 提取日期和域名的正则表达式
    pattern = re.compile(r'<span class="date">(.*?)</span><a href="\/(.*?)/" target="_blank">', re.DOTALL)
    # 在文本中搜索匹配项
    matches = re.findall(pattern, text)
    # 输出匹配项
    result_lists = []
    adress = find.find_adress(ip)
    if matches:
        for match in matches:
            match = list((ip, adress,) + match)
            name = find_company(match[3])
            match.append(name)
            result_lists.append(match)
        return result_lists


def find_company(domain):
    parts = domain.split('.')
    main_domain = parts[-2] + '.' + parts[-1]
    company = find.find_icp(main_domain)
    return company


if __name__ == "__main__":
    print(Fore.BLUE + """
/$$$$$$ /$$$$$$$  /$$$$$$$$        /$$$$$$$                                    /$$        /$$$$$$$$                           /$$                          
|_  $$_/| $$__  $$|__  $$__/       | $$__  $$                                  |__/       |__  $$__/                          | $$                          
  | $$  | $$    $$   | $$  /$$$$$$ | $$  \ $$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$ /$$$$$$$ | $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
  | $$  | $$$$$$$/   | $$ /$$__  $$| $$  | $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$| $$__  $$| $$ /$$__  $$|____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
  | $$  | $$____/    | $$| $$  \ $$| $$  | $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$| $$  \ $$| $$| $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
  | $$  | $$         | $$| $$  | $$| $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$| $$  | $$| $$| $$      /$$__  $$| $$      | $$_  $$ | $$_____/| $$      
 /$$$$$$| $$         | $$|  $$$$$$/| $$$$$$$/|  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$| $$  | $$| $$| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
|______/|__/         |__/ \______/ |_______/  \______/ |__/ |__/ |__/ \_______/|__/|__/  |__/|__/|__/      \_______/ \_______/|__/  \__/ \_______/|__/    """)
    parser = argparse.ArgumentParser(description='ip反查域名以及公司')
    parser.add_argument('--list', '-l', type=str, help='输入文件的名称')
    args = parser.parse_args()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36",
    }
    result_list = []
    with open(args.list, 'r') as f:
        urls = f.readlines()
    for url in urls:
        url = url.strip("\n")
        if "https" in url:
            ip = url.strip("https://")
        elif "http" in url:
            ip = url.strip("http://")
        else:
            ip = url
        if ":" in ip:
            ip = ip.split(":")[0]
        url = "https://site.ip138.com/" + ip
        res = requests.get(url, headers=headers)
        matches = find_domain(res.text, ip)
        if matches is None:
            pass
        else:
            for match in matches:
                result_list.append(match)
    headers = ["IP", "归属地", "时间", "域名", "公司"]
    table = tabulate(result_list, headers, )
    print(Fore.GREEN + table)
