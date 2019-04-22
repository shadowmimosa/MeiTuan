import pandas as pd


def repeated(cityname):
    filepath = "C:\\Users\\ShadowMimosa\\Downloads\\MeiTuan\\My_MeiTuan\\data\\shopinfo\\{}.csv"
    data = pd.read_csv(filepath.format(cityname))
    data.drop_duplicates(subset=["shopName"], keep='first', inplace=True)
    data.to_csv(filepath.format(cityname + '_repeated'), index=False)


if __name__ == "__main__":
    # repeated('宝塔区')
    # repeated('白城')
    repeated('丹阳市')
    repeated('佛冈')