import requests, sys, json
import ast
questions = []
fp1 = open("questions.json","a")

for i in range(180,10000):
	fp2 = open("output","w")
	r = requests.get("https://api.stackexchange.com/questions?page="+str(i)+"&pagesize=100&fromdate=1420070400&todate=1441065600&order=desc&sort=activity&site=stackoverflow&key=Vy89RhnTarQByECuIZzxGQ((")
	fp2.write(str(r))
	response = r.json()
	if(response.has_key("items")==False):
		continue
	print i
	response = response["items"]
	for question in response:
		tags = question["tags"]
#		print question["owner"]
		owner_dict = {}
		for key in question["owner"]:
			owner_dict[str(key)] = question["owner"][key]
		question["owner"] = owner_dict
		if(question["owner"].has_key("user_id")==False):
			continue
		owner_id = question["owner"]["user_id"]
		answer = question["is_answered"]
		answer_id = 0
		if(question.has_key("accepted_answer_id")):
			answer_id = question["accepted_answer_id"]
		id = question["question_id"]
		temp = [tags,owner_id,answer,id,answer_id]
		questions.append(temp)
		fp1.write(str(temp)+"\n")
#		print "I am at the end of the loop"
fp1.close()
fp2.close()
