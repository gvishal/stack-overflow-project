import requests
import json

fp = open("user_data.json", "r")
user_data = json.load(fp)
api_key = "Vy89RhnTarQByECuIZzxGQ(("
out = open("user_id_tag2.json", "w")

total = 0
user_ids = ''

def get_data(user_ids):
    url = "https://api.stackexchange.com/2.2/users/" + user_ids + "/tags?order=desc&sort=popular&site=stackoverflow&key=" + api_key
    r = requests.get(url)
    response = r.json()
    # print response["items"]
    print len(response["items"])
    if not response.has_key("items"):
        print response
        return

    user_tags = {}

    for item in response["items"]:
        user_id = item["user_id"]
        if user_tags.has_key(item["user_id"]):
            user_tags[user_id].append(str(item["name"]))
        else:
            user_tags[user_id] = [str(item["name"])]

    for item in user_tags:
        out.write(str(item) + ' ' + ','.join(user_tags[item]))
        out.write('\n')
    # print user_tags

    # print response

for key in user_data:
    # print total
    if total%50 is 0:
        user_ids = str(key)
        total += 1
        continue
    total += 1
    if total%50:
        user_ids += ';' + str(key)
        # total += 1
        continue
    print user_ids

    get_data(user_ids)

if user_ids:
    get_data(user_ids)


out.close()