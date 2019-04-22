import requests
import json
import jsonpath
import time

from settings import url, uuid, originUrl
from tool.create_token.meituan.createtoken import CreatTokenForMeituan


class Meituan(object):
    def __init__(self, *args, **kwargs):
        self.url = url
        self.cityName = kwargs.get("cityName","北京")
        self.cateId = kwargs.get("cateId",0)
        self.areaId = kwargs.get("areaId",0)
        self.sort = kwargs.get("sort","")
        self.dinnerCountAttrId = kwargs.get("dinnerCountAttrId","")
        self.page = kwargs.get("page",1)
        self.userId = kwargs.get("userId","")
        self.uuid = uuid
        self.platform = kwargs.get("platform",1)
        self.partner = kwargs.get("partner",126)
        self.originUrl = originUrl
        self._token = None
        self.payload = {
            "cityName": self.cityName,
            "cateId": self.cateId,
            "areaId": self.areaId,
            "sort": self.sort,
            "dinnerCountAttrId": self.dinnerCountAttrId,
            "page": self.page,
            "userId": self.userId,
            "uuid": self.uuid,
            "platform": self.platform,
            "partner": self.partner,
            "originUrl": self.originUrl,
            "_token": self._token,
        }
        self.headers = {
            "Host": "bj.meituan.com",
            "Referer": "http://bj.meituan.com/meishi/pn3/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.js; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        }

    def get_response(self):
        response = requests.get(url=self.url, params=self.payload, timeout=6.0, headers=self.headers,verify=False)
        try:
            return json.loads(response.content.decode())
        except:
            self.payload["_token"] = CreatTokenForMeituan.creatToken()
            # print(self._token)
            response = requests.get(url=self.url, params=self.payload, timeout=6.0, headers=self.headers, verify=False)
            return json.loads(response.content.decode())

    def processing_data(self, data):
        data = jsonpath.jsonpath(data, '$..poiInfos')[0]
        return data
    def run(self):
        data = self.get_response()
        data = self.processing_data(data)
        return data


if __name__ == '__main__':
    meituan = Meituan()
    meituan.run()