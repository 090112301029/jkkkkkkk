#导包
import requests

# 发送验证到请求
response_captcha = requests.get(url="http://kdtx-test.itheina.net/api/captchaImage")
#查看喷应
print(response_captcha.status_code)
print(response_captcha.json())
print(response_captcha.text)
#发送登录请求
uuid = response_captcha.json().get("uuid")
login_data = {"username": "admin","password": "HN_2023_test","code": "2","uuid": uuid}
response_login = requests.post(url="http://kdtx-test.itheina.net/api/login", json=login_data)

#查看响应
print(response_login.json())