import requests
import pymongo
import random
import time

client = pymongo.MongoClient()
db = client["ip_pools"]["ip"]


def get_random_proxy():
    '''随机从文件中读取proxy'''
    datas = db.find().limit(150)
    ips = []
    for data in datas:
        ips.append('http://' + data.get("http"))
    proxy = {"http": random.choice(ips)}
    return proxy


if __name__ == '__main__':
    proxy = get_random_proxy()
    print(proxy)
    # http: // i.waimai.meituan.com / openh5 / poi / comments?_ = 1548998967284
    # url = "http://i.waimai.meituan.com/openh5/poi/comments?_={}".format(int(time.time()))
    # print(url)
    # resp = requests.get(url, proxies=proxy)
    # print(resp.status_code)
    # print(resp.text)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36",
        "Referer": "http://i.waimai.meituan.com/openh5/homepage/poilist",
        "Host": "i.waimai.meituan.com",
        "Origin": "http://h5.waimai.meituan.com",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8", }
    data = {
        "startIndex": "0",
        "sortId": "0",
        "multiFilterIds": "",
        "sliderSelectCode": "",
        "sliderSelectMin": "",
        "sliderSelectMax": "",
        "geoType": "2",
        "rankTraceId": "",
        "wm_latitude": "34213074",
        "wm_longitude": "117175680",
        "wm_actual_latitude": "34212690",
        "wm_actual_longitude": "117174720",
    }
    headers[
        "Cookie"] = 'w_actual_lat={}; w_actual_lng={};wm_order_channel=default; openh5_uuid=;'.format(data["wm_actual_latitude"],data["wm_actual_longitude"])

    _ = int(time.time() * 1000)
    url = "http://i.waimai.meituan.com/openh5/homepage/poilist?_=1549072760008"
    resp = requests.post(url, data=data, headers=headers, proxies=proxy)
    print(resp.status_code)
