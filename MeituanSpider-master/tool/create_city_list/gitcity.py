import requests
import json
class MeituanCity(object):
    def __init__(self):
        self.url = "http://www.meituan.com/ptapi/getprovincecityinfo/"
        self.headers = {
            "Host": "bj.meituan.com",
            "Referer": "http://bj.meituan.com/meishi/pn3/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        }
    def get_city_list(self):
        return json.loads(requests.get(self.url, headers=self.headers).content.decode())

    @staticmethod
    def _get_city_list():
        data = json.loads(requests.get("http://www.meituan.com/ptapi/getprovincecityinfo/", headers={
            "Host": "bj.meituan.com",
            "Referer": "http://bj.meituan.com/meishi/pn3/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        }).content.decode())
        city_list = []
        for i1 in data:
            for i in i1.get("cityInfoList"):
                city_list.append(i.get("name"))
        return city_list

    def save_city_list(self):
        with open("city_list.txt","w", encoding="utf-8") as f:
            city_list = []
            for i1 in self.get_city_list():
                for i in i1.get("cityInfoList"):
                    city_list.append(i.get("name"))
            f.write(str(city_list))

if __name__ == '__main__':
    meituancity = MeituanCity()
    meituancity.save_city_list()

