#!/usr/bin/env python
import requests, sys, json
import ast
import time
questions = []
fp1 = open("questions.json", "a")
fp3 = open("tags_questions.json", "a")
fp2 = open("output","a")

# api_key = "Vy89RhnTarQByECuIZzxGQ(("
# vishal
api_key = "A08pO*B1TR5AGvOS4FXflw(("

for i in range(238, 10000):
	print i
	# time.sleep(1)
	# if not i%5:
	# 	print 'sleeping %d' %i
	# 	time.sleep(2)

	r = requests.get("https://api.stackexchange.com/questions?page="+str(i)+"&pagesize=100&fromdate=1420070400&todate=1441065600&order=desc&sort=activity&site=stackoverflow&key=" + api_key)
	response = r.json()

	print 'len: ', len(str(response))

	if response.has_key("backoff"):
		print "backoff detected"
		# print response
		backoff = response["backoff"]
		print backoff
		time.sleep(backoff + 2)

	while r.status_code == 400:
		print 'error 400'
		time.sleep(30)
		r = requests.get("https://api.stackexchange.com/questions?page="+str(i)+"&pagesize=100&fromdate=1420070400&todate=1441065600&order=desc&sort=activity&site=stackoverflow&key=" + api_key)

	if r.status_code != 200:
		fp2.write(str(i) + " " + str(r.status_code) + " " + r.text + "\n")
		continue
	else:
		fp2.write(str(i) + " " + str(r.status_code) + "\n")

	
	if(response.has_key("items")==False):
		continue


	response = response["items"]
	for question in response:
		tags = question["tags"]
		tag_string = ' '.join(tags)
		# print tag_string
#		print question["owner"]
		owner_dict = {}
		for key in question["owner"]:
			owner_dict[str(key)] = question["owner"][key]
		question["owner"] = owner_dict
		owner_id = 0
		if question["owner"].has_key("user_id"):
			owner_id = question["owner"]["user_id"]
		# owner_id = question["owner"]["user_id"]
		is_answered = question["is_answered"]
		answer_id = 0
		if(question.has_key("accepted_answer_id")):
			answer_id = question["accepted_answer_id"]

		question_id = question["question_id"]
		answer_count = question["answer_count"]
		view_count = question["view_count"]
		score = question["score"]

		temp = [tag_string, owner_id, question_id, is_answered, answer_id, answer_count, view_count, score]		
		temp = [str(item) for item in temp]
		final_string = ','.join(temp)
		# print final_string
		fp1.write(final_string)
		fp1.write("\n")
		fp3.write(tag_string)
		fp3.write("\n")

		# temp = [tags, owner_id, answer, id, answer_id]
		# questions.append(temp)
		# fp1.write(str(temp)+"\n")
#		print "I am at the end of the loop"

fp1.close()
fp2.close()
fp3.close()
