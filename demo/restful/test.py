import requests, json

user_info = {'name': 'letian'}
headers = {'content-type': 'application/json'} # 将html文本内容设置为json格式
r = requests.post("http://127.0.0.1:5000/index", data=json.dumps(user_info), headers=headers)
