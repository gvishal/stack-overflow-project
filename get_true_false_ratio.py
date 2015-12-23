from __future__ import division
import operator

#Contains question tags (# = 2624)
list_question_name = []

with open('corrected6.txt','r') as f:
	for line in f:
		list_question_name.append(line)
		list_question_name = map(lambda s: s.strip(), list_question_name)

#Dict for tags of true & false
is_answered_true = {}
is_answered_false = {}

for cntr in list_question_name:
	is_answered_true[cntr] = 0
	is_answered_false[cntr] = 0

#Counting true and false across questions (large file) 
with open('questions.json','r') as m:	
	for line in m:
		for cntr in range(0, len(list_question_name)):
			if list_question_name[cntr] in line and 'True' in line:
				is_answered_true[list_question_name[cntr]] += 1
			

			if list_question_name[cntr] in line and 'False' in line:
				is_answered_false[list_question_name[cntr]] += 1	

ratio_1 = {}
ratio_2 = {}
for cntr in is_answered_true.keys():
	ratio_1[cntr] = 0
	ratio_2[cntr] = 0

for j in is_answered_true.keys():
	if (is_answered_true[j] + is_answered_false[j]) != 0:
		ratio_1[j] = (is_answered_true[j])/(is_answered_true[j]+is_answered_false[j])
	else:
		ratio_1[j] = 0

for j in is_answered_true.keys():
	if (is_answered_true[j] + is_answered_false[j]) != 0:
		ratio_2[j] = (is_answered_false[j])/(is_answered_true[j]+is_answered_false[j])
	else:
		ratio_2[j] = 0

sorted_ratio_1 = sorted(ratio_1.items(), key=operator.itemgetter(1))
sorted_ratio_2 = sorted(ratio_2.items(), key=operator.itemgetter(1))

print ' --------------RATIO_1----------------'
print ''
print ''
for x in sorted_ratio_1:
	print x
print ''
print ''
print ''
print ' --------------RATIO_2----------------'
print ''
print ''
for x in sorted_ratio_2:
	print x

'''			
print 'KEY 	 			TRUE_c			FALSE_c			RATIO_1			RATIO_2'

for j in is_answered_true.keys():
	if (is_answered_true[j] + is_answered_false[j]) != 0:
		print j, is_answered_true[j], is_answered_false[j], is_answered_true[j]/(is_answered_true[j]+is_answered_false[j]), is_answered_false[j]/(is_answered_true[j]+is_answered_false[j])  		
	else:
		print j, is_answered_true[j], is_answered_false[j]		
'''
#Printing O/P	
'''		
print 'TRUE ENTRIES'			
print 'KEY 	 			COUNT'

for j in is_answered_true.keys():
	print j, is_answered_true[j] 

print ''
print ''
print 'FALSE ENTRIES'			
print 'KEY 	 			COUNT'

for j in is_answered_false.keys():
	print j, is_answered_false[j] 
'''