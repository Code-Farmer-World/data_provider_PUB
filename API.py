import requests
import pandas as pd
import json

url = "https://map.dosw.gov.taipei/taipeiwelfare_map/ws/ElderWS.asmx/getClass_T"
# 更新 payload 內容
payload = {
    "FILTER": {
        "x": 304846.3508593684,
        "y": 2770500,
        "dis": 1.5,
        "classtimeS": "00:00",
        "classtimeE": "24:00",
        "startDate": "2025-05-26",
        "endDate": "2025-06-02",
        "polygon": "[[121.56841,50.02608],[121.56820,25.01898],[121.51866,25.01916],[121.51885,25.06430],[121.56841,25.06412]]",
        "geotowns": [],
        "weekDays": ["1", "2", "3", "4", "5", "6", "7"],
        "mainCates": [],
        "subCates": ["運動"],
        "foodTypes": [],
        "keyword": "",
        "coordinates": [0, 0]
    }
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers, json=payload, timeout=30, verify=False)
data = response.json()

# 解析 d 欄位內容
raw_json = json.loads(data["d"])
# 取得 ElderClass 資料，並展開 join 裡的 address、geo、geotown
elderclass_all=[]
for item in raw_json:
    if "ElderClass" in item:
        for ec in item["ElderClass"]:
            join = ec.get("join", {})
            # 扁平化下面欄位
            ec["address_plain"] = join[0].get("address")
            ec["geo_plain"] = join[0].get("geo")
            ec["geotown_plain"] = join[0].get("geotown")
        elderclass_all.extend(item["ElderClass"])

       
df = pd.DataFrame(elderclass_all)

print(df.head())  # 預覽
df.to_csv("台北市據點課程資料.csv", index=False, encoding="utf-8-sig")
print("已匯出 台北市據點課程資料.csv")
