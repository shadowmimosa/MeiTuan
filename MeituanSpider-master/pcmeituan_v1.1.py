from meituan_pc import Meituan
from tool.create_city_list.gitcity import MeituanCity


class MeituanSpider(object):
    def __init__(self):
        self.meituan = Meituan()
        self.citylist = MeituanCity._get_city_list()
        self.datalist = []
        self.num = 1
    def savetomongodb(self):
        pass

    def run(self):
        while True:
            print("开始抓取第{}个城市的商家信息,城市名称：{}".format(self.num,self.meituan.payload["cityName"]))
            data_dict = {}
            data_lists = []

            while True:
                # 抓取一页的数据
                data = self.meituan.run()
                if not data == []:
                    data_lists.append(data)
                    # 翻页抓取
                    self.meituan.payload["page"] += 1
                else:

                    data_dict[self.meituan.payload["cityName"]] = data_lists
                    self.datalist.append(data_dict)
                    self.meituan.payload["page"] = 1
                    break

            if not self.citylist == []:
                # 切换城市
                self.meituan.payload["cityName"] = self.citylist.pop(0)
                self.num+=1
                print(self.datalist)


            else:
                print("抓取完毕")
                print("统计：本次共抓取城市数量为：{}".format(self.num))
                break
a = MeituanSpider()
print(len(a.citylist))
a.run()


