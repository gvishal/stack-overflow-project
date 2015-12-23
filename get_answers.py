#!/usr/bin/env python
import requests, sys, json
import ast
import time

fp1 = open("answers.json", "a")
fp2 = open("output2","a")

api_key = "Vy89RhnTarQByECuIZzxGQ(("
# vishal
# api_key = "A08pO*B1TR5AGvOS4FXflw(("

for i in range(1, 10000):
    print i

    r = requests.get("https://api.stackexchange.com/answers?page="+str(i)+"&pagesize=100&fromdate=1420070400&todate=1441065600&order=desc&sort=activity&site=stackoverflow&key=" + api_key)
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
        r = requests.get("https://api.stackexchange.com/answers?page="+str(i)+"&pagesize=100&fromdate=1420070400&todate=1441065600&order=desc&sort=activity&site=stackoverflow&key=" + api_key)

    if r.status_code != 200:
        fp2.write(str(i) + " " + str(r.status_code) + " " + r.text + "\n")
        continue
    else:
        fp2.write(str(i) + " " + str(r.status_code) + "\n")

    
    if(response.has_key("items")==False):
        continue


    response = response["items"]
    for question in response:

        owner_dict = {}
        for key in question["owner"]:
            owner_dict[str(key)] = question["owner"][key]

        question["owner"] = owner_dict
        owner_id = -1
        reputation = -1
        accept_rate = -1

        if question["owner"].has_key("user_id"):
            owner_id = question["owner"]["user_id"]
        if question["owner"].has_key("reputation"):
            reputation = question["owner"]["reputation"]
        if question["owner"].has_key("accept_rate"):
            accept_rate = question["owner"]["accept_rate"]


        is_accepted = question["is_accepted"]
        question_id = question["question_id"]
        answer_id = question["answer_id"]
        score = question["score"]

        temp = [owner_id, reputation, accept_rate, question_id, is_accepted, answer_id, score]     
        temp = [str(item) for item in temp]
        
        final_string = ','.join(temp)
        # print final_string
        fp1.write(final_string)
        fp1.write("\n")

fp1.close()
fp2.close()
