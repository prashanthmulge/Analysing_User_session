import os
import os.path
import sys

num = 0
user_dict = {}
active_user = {}
# Read the N for distinct paths
if len(sys.argv) == 1:
    print "Error: Please pass the number of distinct paths expected"
    sys.exit()
else:
    num = int(sys.argv[1])

print num

# To retrieve the file and unzip
os.popen("wget http://static.imply.io/takehome/access.log.gz")
os.popen("gunzip -k access.log.gz")
os.open("mkdir out")

fin = open('access.log', 'r')
fout = open('log.txt', 'w')

for line in fin:
    l = line.strip().split(",")
    if active_user.has_key(l[1]):
        continue;
    if os.path.isfile("out/" + l[1] + '.txt'):
        # print l[1], len(user_dict[l[1]])
        f = open("out/" + l[1] + '.txt', 'r+')
        f_list = f.readline().strip().split(",")
        if l[2] not in f_list:
            f.write("," + l[2])
            if len(f_list) == (num - 1):
                active_user[l[1]] = 1
                fout.write(l[1])
        f.close()
    else:
        f = open("out/" +l[1] + ".txt", "w")
        f.write(l[2])
        f.close()


print len(active_user)
fin.close()
fout.close()
# for key in user_dict:
#	fout.write("UserID: " + key)
#	fout.write("\n")
#	#print key, len(user_dict[key])
#	for line in user_dict[key]:
#		fout.write("\t" + line)
os.popen("rm access.log*")
