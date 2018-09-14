#azrael - Simon Tsui, Jason Tung
#SoftDev1 pd8
#K06 -- StI/O: Divine your Destiny!
#2018-09-14F

file = open("occupations.csv", 'r')
lines = file.read().split("\n")
total = dict()
for i in range(1,len(lines)):
    if(len(lines[i]) > 0):
        divpoint = lines[i].rfind(",")
        total[lines[i][:divpoint]] = float(lines[i][divpoint+1:])
file.close()
