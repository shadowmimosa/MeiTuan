import pandas as pd


def deal_phone(data):
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


def repeated(cityname):
    filepath = "C:\\Users\\ShadowMimosa\\Documents\\GitRepository\\MeiTuan\\My_MeiTuan\\data\\shopinfo\\{}.csv"
    data = pd.read_csv(filepath.format(cityname))
    for i, r in data.iterrows():
        tel_num = deal_phone(r["shopPhone"])
        if tel_num:
            data.loc[i, "shopPhone"] = tel_num
        else:
            data = data.drop([i])

    data.drop_duplicates(subset=["shopName"], keep='first', inplace=True)
    data.to_csv(filepath.format(cityname + '_repeated'), index=False)


if __name__ == "__main__":
    # repeated('宝塔区')
    # repeated('白城')
    repeated('丹阳市')
    repeated('佛冈')