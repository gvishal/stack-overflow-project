import get_link,json
import get_patterns
def lst2hash(lst):
#	print lst
	lst.sort()
	string = ''
	for i in lst: 
		string = string + i + ";"
	return string
patterns = get_patterns.get_pattern()
users = {}
txx = 1
page_count = 0
#patterns = [["linux","ubuntu","gcc"],["osx","safari"]]
for tag_pattern in patterns:
	print page_count
 	print tag_pattern
	print txx
	txx = txx + 1
	string = ''
	for i in range(0,len(tag_pattern)):
		if(i<(len(tag_pattern)-1)):
			string = string + tag_pattern[i]+";"
		else:
		 	string = string + tag_pattern[i]
	answers = []
	###Trying to get all the questions of this paticular tag
	page_no = 1
	while (1):
 		link = "https://api.stackexchange.com/questions?page="+str(page_no)+"&pagesize=100&fromdate=1420070400&todate=1441065600&order=desc&sort=activity&tagged="+str(string)+"&site=stackoverflow&key=Vy89RhnTarQByECuIZzxGQ(("
		r = get_link.download(link) 
		page_count = page_count + 1
		page_no = page_no + 1
		response = r.json()
		if(response.has_key("items") and len(response["items"])>0):
			for question in response["items"]:
				if(question.has_key("accepted_answer_id")):
					answers.append(question["accepted_answer_id"])
		else:
	 		break
#	print "No of answers"
#	print len(answers)
	x = (len(answers)/100) +1
	for i in range(0,x):
		string = ''
		for j in range(0,100):
			index = (100*i)+j
#			print index
			if(index>=(len(answers))):
				break
			if(index == len(answers)-1):
				string = string + str(answers[index])
				break
			elif(i!= x and j==99):
				string = string + str(answers[index])
			else:
				string = string+str(answers[index])+";"
		link = "https://api.stackexchange.com/2.2/answers/"+str(string)+"?order=desc&sort=activity&site=stackoverflow&key=Vy89RhnTarQByECuIZzxGQ(("
		r = get_link.download(link)
		page_count = page_count + 1
		response = r.json()
		if(response.has_key("items") and len(response["items"])>0):
			for answer in response["items"]:
#		if(answer.has_key("user_id")==False):
#					print "I am continuing"
#					continue
#print type(answer["owner"])
				temp = {}
				for key in answer["owner"]:
					temp[str(key)] = answer["owner"][key]

				#print temp
				if(temp.has_key('user_id')==False):
					continue
				user_id = temp['user_id']
				if(users.has_key(user_id)==False):
					users[user_id] = {}
#				print type(tag_pattern)
				y = lst2hash(tag_pattern)
				if(users[user_id].has_key(y)==False):
					users[user_id][y] = 0
				users[user_id][y] = users[user_id][y] + 1

print users
fp = open("user_data.json","w")
json.dump(users,fp)
fp.close()
