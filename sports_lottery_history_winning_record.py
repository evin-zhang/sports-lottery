import requests
import json
import csv
headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=2289&isVerify=1&pageNo=1'
r = requests.get(url, headers=headers)
data = r.json()
items = data['value']['list']
f = open('csv_file.csv','w',encoding='utf-8')
csv_write = csv.writer(f)
csv_write.writerow(['lotteryDrawNum','lotteryDrawResult','lotteryDrawTime'])
for item in items:
    csv_write.writerow([item['lotteryDrawNum'],item['lotteryDrawResult'],item['lotteryDrawTime']
])
f.close


