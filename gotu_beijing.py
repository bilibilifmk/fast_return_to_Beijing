import requests
import json
import time

bufbody = "将body内容复制到这里"

def push():
    global bufbody
    post_url='https://yqgz.beijing.gov.cn/service/returnBj/checkPersonApplyStatus'
    res=requests.post(post_url,data = bufbody ,headers={"accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json",
        "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"})
    print(res)
    print(res.text)
    return res.text

if __name__ == '__main__':
    checkState = 0
    while True:
        try:
            res = json.loads(push())
            State = res["data"]['checkState']
            if State != checkState and checkState != 0 :
                checkState = State
                print("状态发生改变！！！！请尽快查看")
                #这条可注释 需要bark app进行推送消息到手机
                requests.get("https://api.day.app/填写你的bark app key /%E8%BF%9E%E6%8E%A5%E7%8A%B6%E6%80%81%E6%94%B9%E5%8F%98%E8%AF%B7%E7%82%B9%E5%87%BB%E9%93%BE%E6%8E%A5%E6%9F%A5%E7%9C%8B?url=https://yqgz.beijing.gov.cn/wssryfw/")
        except:
                print("请求故障")
        time.sleep(60)
