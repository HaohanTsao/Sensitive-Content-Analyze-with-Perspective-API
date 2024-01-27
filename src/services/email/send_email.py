# %%
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(from_email, app_password, to_email, subject, text):
    msg = MIMEMultipart()
    msg["from"] = from_email
    msg["to"] = to_email
    msg["subject"] = subject

    msg.attach(MIMEText(text))

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(from_email, app_password)  # 登入
            smtp.send_message(msg)  # 寄送郵件
            print("Email sent successfully.")
        except Exception as e:
            print("Error message: ", e)
