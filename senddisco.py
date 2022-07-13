# 모듈 없다는 오류가 날 경우 requests 모듈 설치
# 설치 방법 : pip install requests

import requests
import sys
import configparser
import os

# info
senddisco_version = 1.0
print('senddisco 버전:', senddisco_version)
# 윈도우 (exe)
# senddisco_path = sys.executable[:-13]
# 우분투, 윈도우 (.py)
senddisco_path = os.path.dirname(os.path.realpath(__file__))
print('senddisco 경로:', senddisco_path)

# senddisco.ini파일에서 정보 불러오기
config = configparser.ConfigParser()
config.read(f'{senddisco_path}/senddisco.ini')
settings = config['SETTINGS']
webhookURL = settings["webhookURL"]
username = settings["username"]
avatar_url = settings["avatar_url"]

# 메시지 변수 받기
if len(sys.argv) >= 2:
    message = sys.argv[1]
    print('username :', username)
    print('메시지 내용 :', message)
else:
    print('메시지 내용이 없습니다.')
    print('사용법 : python3 senddisco.py "메시지 내용"')
    sys.exit()


# requests모듈로 json 전송
data = {
    "content": message,
    "username": username,
    "avatar_url": avatar_url,
}


result = requests.post(webhookURL, json=data)
if 200 <= result.status_code < 300:
    print(f"Webhook sent {result.status_code}")
else:
    print(f"Not sent with {result.status_code}, response:\n{result.json()}")
