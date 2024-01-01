from content_censor import Censor
import json
from dotenv import load_dotenv
load_dotenv()
import os

API_KEY = os.getenv("API_KEY")
SENSITIVE_KEYWORDS = ['外送茶']
CONTENT = '''台灣外送茶+賴gg9875或TG搜索@gg9875加入領取優惠約妹立減1-5k

買1送1買2送2買幾送幾送現金卷+送絲襪+免房費+Vip會員福利

淫液：早上10:00-淩晨02:00（提早1小時預約優選好妹）

消費：不點數、不轉賬、不匯款、不強迫消費-可免費退換

約會：雙北-新竹-台中-彰化-高雄-台南...外約/住家/旅館

類型：各行各業本土妹純兼職選擇性多日.巴.韓.俄混血兒

外貌是基本的，服務是頂級的

錢本來就該花在對的地方

享受到你應該得到的享受

內行人不問外行話

快來找小樂尋歡作樂舒壓放鬆吧！

小樂的Line洽詢：gg9875或59551

小樂telegram洽詢：@gg9875

TG簽到領取優惠：@slinegg9875

看更多正妹官網：shanshan.7788.tw

'''

def main():
    content_censor = Censor(api_key=API_KEY, sensitive_keywords=SENSITIVE_KEYWORDS)
    content = CONTENT

    output = content_censor.analyze(content=content)
    output = json.dumps(output, indent=2, ensure_ascii=False)
    print(output)

if __name__ == "__main__":
    main()
