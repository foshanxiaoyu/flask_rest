import requests

Base = 'http://127.0.0.1:5000/'
data = [{'likes':4523,'views':22034,'name':'I like C plus'},
        {'likes':343,'views':22057,'name':'I like Python'},
        {'likes':5434,'views':22054,'name':'I like Java'},
        {'likes':5444,'views':22786,'name':'I like Mongodb'},]
for i in range(len(data)):
    res = requests.post(Base + 'video/'+str(i),data[i])
    print(res.json())
    
# res = requests.post(Base + 'hehe')
# res = requests.get(Base + 'hehe/bill')
input()
res = requests.delete(Base + 'video/0')
print(res)
input()
res = requests.get(Base + 'video/2')
print(res.json())

