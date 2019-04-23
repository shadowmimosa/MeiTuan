import requests
import urllib3
import time
import json
import random
import pandas as pd


class MeiTuan(object):
    def __init__(self, city="", keyword=""):
        self.city = city
        self.keyword = keyword
        self.search_url = "https://maf.meituan.com/search?key=be9427ec-bca4-4bfa-b981-9314f6a1adc7&location=118.796623%2C32.059352&region=CITY&orderby=weight&radius=50000&pageSize=20&page={}&city={}&keyword={}&wm_latitude=32059352&wm_longitude=118796623&wm_actual_latitude=&wm_actual_longitude=&_=1555823134637&X-FOR-WITH=MXltohpq5fyeO8evRZFLgv%2FBD7EdhVrmidxfB8NM%2Fc7EekxXP%2FvV%2FXtmXs38StwM3JQ8PJsn9moKvOvrpye1xcisbzBBQuhYfdABirTEFaRQaJ2FrwiTbVztaJ85aexLRZmgaqTJi9qbRN%2B4gzX77A%3D%3D"
        self.homepage_url = "http://i.waimai.meituan.com/openh5/homepage/poilist?_=1555834031305&X-FOR-WITH=apN6l24WQrK3ayVg%2BHwS80GV%2FBox3IB9mB7q3CH8pvxwyr%2FAthD68zMOyx1ojQQjlRpD0pNI2VL9DwEjmmYoPy6KIWZl2%2FkBmjxR2DjO8B0HWaVbFsxSB5bwnXEthdrLpq07W%2FhsEbNssjnOgXa6DA%3D%3D"
        self.shopinfo_url = "http://i.waimai.meituan.com/openh5/poi/info?_=1555836588703&X-FOR-WITH=apN6l24WQrK3ayVg%2BHwS80GV%2FBox3IB9mB7q3CH8pvzDH%2BgXrvXht2Fw9xXiS8jaj%2FbDymS%2BSHYm39UOHh%2FFeqhYIiwSaLso8qzC1mfBtYmL5gOFFygM66yoTaL68WiK89GwkL9Tlk0Vorf0tz9n6w%3D%3D"
        self.search_header = {
            "Host": "maf.meituan.com",
            "Connection": "keep-alive",
            "Accept": "application/json",
            "Origin": "http://h5.waimai.meituan.com",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
            "Referer": "http://h5.waimai.meituan.com/waimai/mindex/poipicker",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        self.homepage_header = {
            "Host":
            "i.waimai.meituan.com",
            # Proxy-Connection: keep-alive
            "Accept":
            "application/json",
            "Origin":
            "http://h5.waimai.meituan.com",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
            "Content-Type":
            "application/x-www-form-urlencoded",
            "Referer":
            "http://h5.waimai.meituan.com/waimai/mindex/home",
            "Accept-Encoding":
            "gzip, deflate",
            "Accept-Language":
            "zh-CN,zh;q=0.9",
            "Cookie":
            "_ga=GA1.3.1217321615.1555596854; _lxsdk_cuid=16a30cc57b8c8-035c98b09aa767-9333061-1fa400-16a30cc57b9c8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _gid=GA1.3.457478249.1555764190; wm_order_channel=default; au_trace_key_net=default; terminal=i; w_utmz=\"utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)\"; w_uuid=IF7nje9cK6zLOC9FGq5UPUdNOPNz5bGU3mryWXYCOemPCPRYJFiKVOkV3Glivwhx; __mta=256809908.1555764194983.1555764194983.1555768166452.2; utm_source=0; wx_channel_id=0; IJSESSIONID=1vcld5l3s32s0fpceg0aehv2w; iuuid=6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B; latlng=23.222179%2C113.264696%2C1555781882793; ci=20; cityname=%E5%B9%BF%E5%B7%9E; backurl=http://i.meituan.com/zpay/284712; _lxsdk=6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B; i_extend=H__a100040__b1; mtcdn=K; webp=1; __utma=74597006.166703875.1555781884.1555781884.1555781884.1; __utmc=74597006; __utmz=74597006.1555781884.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); openh5_uuid=6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B; uuid=6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B; openh5_uuid=6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B; w_visitid=1e45b6f9-49e2-492f-9888-d519618ab514; w_latlng={}; _lxsdk_s=16a3e125c0e-fcc-47c-0fe%7C%7C28"
            # "_ga=GA1.3.1217321615.1555596854; _lxsdk_cuid=16a30cc57b8c8-035c98b09aa767-9333061-1fa400-16a30cc57b9c8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _gid=GA1.3.457478249.1555764190; wm_order_channel=default; au_trace_key_net=default; terminal=i; w_utmz=\"utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)\"; w_uuid=IF7nje9cK6zLOC9FGq5UPUdNOPNz5bGU3mryWXYCOemPCPRYJFiKVOkV3Glivwhx; __mta=256809908.1555764194983.1555764194983.1555768166452.2; utm_source=0; wx_channel_id=0; IJSESSIONID=1vcld5l3s32s0fpceg0aehv2w; iuuid=6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B; latlng=23.222179%2C113.264696%2C1555781882793; ci=20; cityname=%E5%B9%BF%E5%B7%9E; backurl=http://i.meituan.com/zpay/284712; _lxsdk=6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B; i_extend=H__a100040__b1; mtcdn=K; webp=1; __utma=74597006.166703875.1555781884.1555781884.1555781884.1; __utmc=74597006; __utmz=74597006.1555781884.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); openh5_uuid=6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B; uuid=6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B; openh5_uuid=6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B; w_latlng=31332901,120677863; _lxsdk_s=16a3eef4196-e01-40a-790%7C%7C3"
            # '"_ga": "GA1.3.1217321615.1555596854","_lxsdk_cuid":"16a30cc57b8c8-035c98b09aa767-9333061-1fa400-16a30cc57b9c8","_lx_utm": "utm_source%3DBaidu%26utm_medium%3Dorganic","_gid": "GA1.3.457478249.1555764190","wm_order_channel": "default","au_trace_key_net": "default","terminal": "i","w_utmz":"utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)","w_uuid":"IF7nje9cK6zLOC9FGq5UPUdNOPNz5bGU3mryWXYCOemPCPRYJFiKVOkV3Glivwhx","__mta":"256809908.1555764194983.1555764194983.1555768166452.2","utm_source": "0","wx_channel_id": "0","IJSESSIONID": "1vcld5l3s32s0fpceg0aehv2w","iuuid":"6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B","latlng": "23.222179%2C113.264696%2C1555781882793","ci": "20","cityname": "%E5%B9%BF%E5%B7%9E","backurl": "http://i.meituan.com/zpay/284712","_lxsdk":"6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B","i_extend": "H__a100040__b1","mtcdn": "K","webp": "1","__utma":"74597006.166703875.1555781884.1555781884.1555781884.1","__utmc": "74597006","__utmz":"74597006.1555781884.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)","openh5_uuid":"6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B","uuid":"6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B","openh5_uuid":"6245B9D92A1243663F6F5935F2E5900058266E99C3D75BE53A2FC56EA115D40B","w_visitid": "1e45b6f9-49e2-492f-9888-d519618ab514","w_latlng": "32059352,118796623","_lxsdk_s": "16a3e125c0e-fcc-47c-0fe%7C%7C28"'
        }

        self.data = {
            "startIndex": "0",
            "sortId": "0",
            "multiFilterIds": "",
            "sliderSelectCode": "",
            "sliderSelectMin": "",
            "sliderSelectMax": "",
            "geoType": "2",
            "rankTraceId": "",
            "wm_latitude": "31332901",
            "wm_longitude": "120677863",
            "wm_actual_latitude": "",
            "wm_actual_longitude": "",
            "_token": ""
        }

    def get_session(self):
        """创建 session 示例，以应对多线程"""

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        #设置重连次数
        requests.adapters.DEFAULT_RETRIES = 5
        # 设置连接活跃状态为False
        session = requests.session()
        session.keep_alive = False
        session.verify = False

        adapter = requests.adapters.HTTPAdapter(max_retries=3)
        #将重试规则挂载到http和https请求
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        return session

    def deal_re(self, **kwargs):
        """requests of get"""

        url = kwargs["url"]
        # url = kwargs.get("url")
        header = kwargs.get("header")
        try:
            data = kwargs.get("data")
        except:
            data = None

        sesscion_a = self.get_session()

        print("---> 开始请求网址：{}".format(url))
        start_time = time.time()
        try:
            if not data:
                resp = sesscion_a.get(url, headers=header, timeout=(3.2, 30))
            else:
                resp = sesscion_a.post(
                    url, headers=header, data=data, timeout=(3.2, 30))
        except Exception as exc:
            print(
                "---> The error is {}, and the website is {}. Now try again just one time."
                .format(exc, url))
            self.deal_re(url=url, header=header, data=data)

        end_time = time.time()
        if resp.status_code == 200:
            print("---> {} 请求成功！共耗时{:.3}秒\n".format(url,
                                                    end_time - start_time))
            random_time = random.randint(3, 10)
            print("---> 现在开始睡眠 {} 秒\n".format(random_time))
            time.sleep(random_time)

            return resp.text
        else:
            print("---> {} 请求失败！状态码为{}，共耗时{:.3}秒\n".format(
                url, resp.status_code, end_time - start_time))
            return None

    def search_city(self):

        url = self.search_url.format('1', self.city, self.keyword)

        with open(
                './data/result_city/{}.json'.format(self.city),
                'w+',
                encoding='utf-8') as fn:
            fn.write(self.deal_re(url=url, header=self.search_header))

    def random_list(self, lenght):
        num_list = []
        i = 0
        lenght = int(lenght / 20)

        for j in range(20):
            random_num = random.randint(i, i + lenght)
            if random_num not in num_list:
                num_list.append(random_num)
            else:
                num_list.append(random.randint(i + 1, i + lenght))
            i += lenght

        return num_list

    def homepage_list(self):
        with open(
                './data/result_city/{}.json'.format(self.city),
                'r',
                encoding='utf-8') as fn:
            sel_list = json.loads(fn.read())
        length = len(sel_list["result"]["pois"])
        random_count = self.random_list(length)

        for index in range(length):
            if index not in random_count:
                continue
            else:
                value = sel_list["result"]["pois"][index]
                location = value["location"].split(',')
                header = self.homepage_header
                header["Cookie"] = header["Cookie"].format(location[1].replace(
                    '.', '') + ',' + location[0].replace('.', ''))
                data = self.data
                data["wm_longitude"] = location[0].replace('.', '')
                data["wm_latitude"] = location[1].replace('.', '')
                # data["startIndex"] = count
                shop_list = self.deal_re(
                    url=self.homepage_url, header=header, data=data)

                with open(
                        './data/shoplist/{}.json'.format(self.city),
                        'a',
                        encoding='utf-8') as fn:
                    fn.write(shop_list + '\n')
                    print("---> Writing successed.\n")

    def get_shop_info(self):
        shopid_list = []
        with open(
                './data/shoplist/{}.json'.format(self.city), 'r',
                encoding='utf-8') as fn:
            for value in fn.readlines():
                for shopid in json.loads(value)["data"]["shopList"]:
                    if shopid not in shopid_list:
                        shopid_list.append(shopid["mtWmPoiId"])

        header = self.homepage_header
        data = {
            "geoType": "2",
            "mtWmPoiId": "901935722373382",
            "dpShopId": "-1",
            "source": "shoplist",
            "skuId": "",
            "wm_latitude": "31327572",
            "wm_longitude": "120674535",
            "wm_actual_latitude": "",
            "wm_actual_longitude": "",
            "_token": ""
        }
        for value in shopid_list:
            header[
                "Referer"] = "http://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId={}&source=shoplist&initialLat=31.327572&initialLng=120.674535&actualLat=&actualLng=".format(
                    value)
            data["mtWmPoiId"] = value

            shop_info = self.deal_re(
                url=self.shopinfo_url, header=header, data=data)

            with open(
                    './data/shopinfo/{}.json'.format(self.city),
                    'a',
                    encoding='utf-8') as fn:
                fn.write(shop_info + '\n')

        pass


class DataClean(object):
    def __init__(self, city=""):

        self.city = city

    def deal_phone(self, data):

        telphone = ""
        data = eval(data)
        if type(data) == list:
            for value in data:
                if len(value) == 11 and '-' not in value:
                    telphone = telphone + value + ' '
                else:
                    continue
            if len(telphone) == 0:
                return False
            else:
                return telphone
        else:
            return False

    # def down_pic(self,info_csv):
    # url = "http://i.waimai.meituan.com/ajax/v6/poi/qualification"
    #     if len(eval(info_csv))==0:
    #         resp=MeiTuan().deal_pic()
    #     pass

    def bulid_csv(self):

        info_csv = pd.DataFrame(columns=[
            "shopName", "shopAddress", "shopPhone", "licencePics",
            "poiQualificationInfoUrl"
        ])

        shop_info_list = []
        with open(
                './data/shopinfo/{}.json'.format(self.city), 'r',
                encoding='utf-8') as fn:
            for value in fn.readlines():
                shop_info_list.append(json.loads(value))

        for value in shop_info_list:
            info_csv = info_csv.append({
                "shopName":
                value["data"]["shopName"],
                "shopAddress":
                value["data"]["shopAddress"],
                "shopPhone":
                value["data"]["shopPhone"],
                "licencePics":
                value["data"]["licencePics"],
                "poiQualificationInfoUrl":
                value["data"]["poiQualificationInfo"]["url"]
            },
                                       ignore_index=True)

        info_csv.drop_duplicates(
            subset=["shopName"], keep='first', inplace=True)

        for i, r in info_csv.iterrows():
            tel_num = self.deal_phone(r["shopPhone"])
            if tel_num:
                info_csv.loc[i, "shopPhone"] = tel_num
            else:
                info_csv = info_csv.drop([i])

        if len(info_csv) < 100:
            info_csv.to_csv(
                './data/finally/lack/{}.csv'.format(self.city), index=False)
        else:
            # self.down_pic(info_csv)
            info_csv.to_csv(
                './data/finally/{}.csv'.format(self.city), index=False)

    def run(self):
        self.bulid_csv()


def main(city_list=["浑江区"]):
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    start_time = time.time()
    for value in city_list:
        spider = MeiTuan(value, value)
        spider_clean = DataClean(value)
        spider.search_city()
        spider.homepage_list()
        spider.get_shop_info()
        spider_clean.run()

    print("---> 总计耗时为 {} 秒".format(time.time() - start_time))


if __name__ == "__main__":
    main(["宝塔区", "白城", "长乐市", "丹阳市", "佛冈"])

    # spider = MeiTuan('hun','hun')
    # spider.random_list(20)
