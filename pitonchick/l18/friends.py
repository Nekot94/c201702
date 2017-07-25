from json import loads
from urllib.request import urlopen
from time import sleep

friends = []
# user_id = '305419418'
# user_id = '394052697'
user_id = '365561911'
data = urlopen('https://api.vk.com/method/friends.get?user_id=' + user_id + "&fields=nickname")
data = data.read().decode("utf-8")
data = loads(data)
response =data["response"]
friends_id = [uid["uid"] for uid in response]
friends_names = [name["first_name"] + " " + name["last_name"] for name in response]
# print(friends_id)
# print(friends_names)

for f_id,f_name in zip(friends_id, friends_names):
	data = urlopen('https://api.vk.com/method/friends.get?user_id=' + str(f_id))
	data = data.read().decode("utf-8")
	data = loads(data)
	# print(data)
	try:
		friends_friends_id = data["response"]
	except:
		continue
	friends.append([f_name, len(set(friends_friends_id) & set(friends_id))])
	sleep(0.0001)
	# print(".", end="")
# print()
friends.sort(key=lambda e: -e[1])
print(friends)

