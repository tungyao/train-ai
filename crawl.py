import json
import time

import requests


def getCap(n):
    req = {
        "catalogNodeId": "313",
        "pageNumber": f"{n}",
        "querySortBySign": "0",
        "showOutSockProduct": "1",
        "showDiscountProduct": "1",
        "keyword": "",
        "queryBeginPrice": "",
        "queryEndPrice": "",
        "lastParamName": "",
        "parameterCondition": "",

    }
    headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "167",
        "Cookie": "cookies_save_operation_code_mark=A; computerKey=1f256d3251ccbcb235b9; lotteryKey=e236b02dcfd0548a54e3; guidePage=true; AGL_USER_ID=48902656-4093-41ea-8c46-ae6b428be888; noLoginCustomerFlag2=379f90f9e3cba9d74c2e; lctcn=7127BE4CED63F6C33B9FB5E8E949D1D8A60785412DF4EEC0F4D18D558544A78E9EE8P27; searchHistoryRecord=SGM4056-6.8YTDE8G%EF%BC%9A%E9%9F%B3%E9%A2%91%E6%94%BE%E5%A4%A7%E5%99%A8%EF%BC%9A%E5%BC%80%E5%8F%91%E6%9D%BF; cpx=1; Qs_lvt_290854=1717145974%2C1717376569%2C1718242484%2C1718592883%2C1719278889; Qs_pv_290854=900669046872104100%2C2008220945252268800%2C3175864763982422000%2C511644133585882300%2C2539528364675535000; Hm_lvt_e2986f4b6753d376004696a1628713d2=1717376569,1718092421,1718242485,1719278890; Hm_lpvt_e2986f4b6753d376004696a1628713d2=1719278890; PRO_NEW_SID=ede33ee1-780d-4891-be11-e8d273978b94; isLoginCustomerFlag=1507588A; noLoginCustomerFlag=8a76342cc6cffa322fb7; SID=b2068fd6-81b7-4240-ad86-f4c823c644b9; SID.sig=KierXkLkEfsID12Y5z_e63x92R3gQS69TBpNy1v1R3Y; Hm_lvt_66fbab03894c99c6f9a3c475e689e550=1717376683,1718242492,1719278929; Hm_lpvt_66fbab03894c99c6f9a3c475e689e550=1719278929; customer_info=2-0-0-0; acw_tc=76b20fec17192839202208054e2013fc3a9261d3fe905f3433e7fb991bd683; show_out_sock_product=1",
        "Host": "list.szlcsc.com",
        "Origin": "https://list.szlcsc.com",
        "Referer": "https://list.szlcsc.com/catalog/313.html",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
    }
    resp = requests.post("https://list.szlcsc.com/products/list",
                         data=req, headers=headers)
    if resp.status_code == 200:
        resp = json.loads(resp.text)
        list = resp["productRecordList"]
        dt = {
            "Model": "",
            "Package": "",
            "Type": "",
            "Voltage": "",
            "Cap": "",
            "Precision": "",
            "Resistance": "",
            "Watt": "",
            "Inductance": "",
            "Electricity": "",
            "Body": ""
        }
        dts = []
        for i in list:
            dtt = dt
            dtt["Package"] = i["lightStandard"]
            dtt["Type"] = i["lightCatalogName"]
            dtt["Model"] = i["lightProductModel"]
            if "容值" in i["paramLinkedMap"]:
                dtt["Precision"] = i["paramLinkedMap"]["容值"].replace("±", "")
            else:
                continue
            if "精度" in i["paramLinkedMap"]:
                dtt["Precision"] = i["paramLinkedMap"]["精度"].replace("±", "")
            else:
                continue
            if "额定电压" in i["paramLinkedMap"]:
                dtt["Precision"] = i["paramLinkedMap"]["额定电压"].replace("±", "")
            else:
                continue
            dtt["Body"] = (i["lightBrandName"] +
                           i["lightCatalogName"] +
                           i["lightProductModel"] +
                           i["lightProductName"] +
                           i["lightStandard"] +
                           i["productArrange"] +
                           i["productMinEncapsulationUnit"] + json.dumps(i["paramLinkedMap"], ensure_ascii=False).
                           replace(" ", "").replace("\"", "").replace("{", "").replace("}", "").replace(":", ""))
            dts.append(dtt)
        return dts


if __name__ == "__main__":
    max = 30
    for i in range(4, max):
        print(f"正在爬取第{i}页")
        dts = getCap(i)
        with open(f"data/cap{i}.json", "w", encoding="utf-8") as f:
            json.dump(dts, f, ensure_ascii=False)
        time.sleep(5)
