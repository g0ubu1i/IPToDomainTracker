import requests
import json


def find_icp(domain):
    url = "https://api.uutool.cn/beian/icp/"

    headers = {
        "Host": "api.uutool.cn",
        "Content-Length": "18",
        "Sec-Ch-Ua": '"Chromium";v="119", "Not?A_Brand";v="24"',
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Origin": "https://uutool.cn",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://uutool.cn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Priority": "u=1, i",
    }

    data = {
        "domain": "{}".format(domain),
    }

    response = requests.post(url, headers=headers, data=data)
    if response.text:
        response_data = json.loads(response.text)
        if response_data['data']['is_icp'] == 1:
            icp_org_data = response_data['data']['icp_org']
            return icp_org_data
        else:
            return "未查询到备案信息"
    else:
        return "未查询到备案信息"
