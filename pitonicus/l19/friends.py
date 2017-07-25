from json import loads
from urllib.request import urlopen
from time import sleep

friends = []
your_id = "229560014"
data = urlopen("https://api.vk.com/method/friends.get?user_id=" + your_id + "&v=5.52&fields=nickname")
data = data.read().decode("utf-8")
data = loads(data)
# print(data)
friends_ids = [f_id["id"] for f_id in data['response']['items']]
friends_names = [f_name["first_name"] + " " + f_name["last_name"] for f_name in data['response']['items']]
# print(friends_ids)
# print(friends_names)
for friend, name in zip(friends_ids, friends_names):
	data = urlopen("https://api.vk.com/method/friends.get?user_id=" + str(friend) + "&v=5.52")
	data = data.read().decode("utf-8")
	data = loads(data)
	try:
		your_friend_ids = data['response']['items']
	except KeyError:
		continue

	friends.append([name, len(set(friends_ids) & set(your_friend_ids))])

	# print(your_friend_ids)
	sleep(0.0001)
friends.sort(key=lambda e: -e[1])

print(friends)

