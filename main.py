import os
import sys

num = 0
user_dict = {}
active_user = {}
#Read the N for distinct paths 
if len(sys.argv) == 1:
	print "Error: Please pass the number of distinct paths expected"
	sys.exit()
else:
	num = int(sys.argv[1])

print num

#To retrieve the file and unzip 
os.popen("wget http://static.imply.io/takehome/access.log.gz")
os.popen("gunzip -k access.log.gz")

fin = open('access.log', 'r')
fout = open('log.txt', 'w')

for line in fin:
	l = line.strip().split(",")
	if active_user.has_key(l[1]):
		continue;
	if user_dict.has_key(l[1]):
		#print l[1], len(user_dict[l[1]])
		if l[2] in user_dict[l[1]]:
			continue
		else:
			user_dict[l[1]].append(l[2])

		if len(user_dict[l[1]]) == num:
			fout.write("UserID: " + l[1] + "\n")
			active_user[l[1]] = 1
			del user_dict[l[1]]
			continue;
	else:
		li =[]
		li.append(l[2])
		user_dict[l[1]] = li
print len(user_dict)
print len(active_user)
fin.close()
fout.close()
os.popen("rm access.log*")
