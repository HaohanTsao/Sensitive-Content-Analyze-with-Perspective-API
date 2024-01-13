import requests

url = ""

# 設定要測試的數據
data = {
    "type": "INSERT",
    "table": "webhook_test",
    "record": {
        "id": 1,
        "created_at": "2024-01-12T03:12:09.175032+00:00",
        "content_raw": "test test test",
        "title_raw": "約炮",
        "user_id": "03cea6d6-ca78-4a0a-a89b-c58d2fb1fece",
        "is_deleted": True,
    },
    "old_record": {},
}

# 發送POST請求
response = requests.post(url, json=data)

# 檢查響應
if response.status_code == 200:
    print("請求成功！")
else:
    print(f"請求失敗，狀態碼：{response.status_code}")
    print("響應內容：", response.text)
