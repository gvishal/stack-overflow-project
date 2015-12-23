import re


dates = ['2008','2010','2012','2013','2014','2015','-404']
with open('output2.txt','rU') as f:
  with open('corrected.txt','a') as myfile:
    for line in f:
      if any(ext in line for ext in dates):
        myfile.write(line) 
      else:
        string_temp = re.sub('[0-9][0-9][0-9]+','',line)
        myfile.write(string_temp)
    
