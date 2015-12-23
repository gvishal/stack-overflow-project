import json

user_data = open("user_data.json", "r")
user_id_tag = open("user_id_tag.json", "r")
tag_pattern_count = open("tag_pattern_count.txt", "r")
tag_recommendation = open("tag_recommendation.json", "w")

user_data = json.load(user_data)

recommendation = {}

for line in user_id_tag.readlines():
    line = line.strip()
    user_id, user_tags = line.split(" ")
    user_tags = user_tags.split(",")
    # print user_id, user_tags

    if not user_data.has_key(user_id):
        continue

    # get user tag from file
    user_tag = str(user_data[user_id].keys()[0])
    # print user_tag

    # update count for user_tag
    if not recommendation.has_key(user_tag):
        recommendation[user_tag] = {}

    tag_pattern_count.seek(0)
    for p in tag_pattern_count.readlines():
        pattern = p.strip().split(" ")[:-1]
        count = 0
        for t in pattern:
            if t in user_tags:
                count += 1
                # break

        # break
        if count == len(pattern):
            # print pattern
            pat = ';'.join(pattern)
            if not recommendation[user_tag].has_key(pat):
                recommendation[user_tag][pat] = 0
            recommendation[user_tag][pat] += 1

    # break


    # for t in user_tags:
    #     if not recommendation[user_tag].has_key(t):
    #         recommendation[user_tag][t] = 0
    #     recommendation[user_tag][t] += 1

json.dump(recommendation, tag_recommendation)
# print recommendation