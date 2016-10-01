import urllib
import re

url = raw_input("Enter the web link : ")
p = urllib.urlopen(url)
a=p.read()

pattern = re.compile('img .*?src="(.*?)"', re.IGNORECASE)
a = re.findall(pattern , a)

for i in a:
	 	f=open("new.txt","w")
	 	f.write(url + i +"\n")
		f.close()
		
	
