import sqlite3
import csv

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()


#Prints out course grades per student via matching roster.id to courses.id
command = """SELECT name, mark, roster.id
    FROM roster, courses
    WHERE courses.id = roster.id"""
c.execute(command)
for row in c:
    print(row)


#Prins out averages by student names and their averages
avgs = {}
sum = 0
lastPer = ""
numCourses = 0
command = """SELECT name, mark
    FROM roster, courses
    WHERE courses.id = roster.id"""
c.execute(command)
for row in c:
    if row[0] != lastPer:
        if numCourses != 0:
            avgs[lastPer] = int(sum/numCourses) # rounds down
        lastPer = row[0] #update current name to be tested
        sum = 0 #reset
        numCourses = 0 #reset
    sum += row[1]
    numCourses += 1
avgs[lastPer] = int(sum/numCourses) #cuz last person does't have a row after to test with
print (avgs)

#prints out name, id, and average
pplList = {}
command = """
    SELECT name, id
    FROM roster"""
c.execute(command)
for row in c:
    pplList[row[0]] = (row[1],  avgs[row[0]]) #first value is id, second is avg
print (pplList)


command = "CREATE TABLE if not exists peeps_avg(id INTEGER, average INTEGER)"
c.execute(command)
for key in pplList:
    params = (pplList[key][0], pplList[key][1])
    #command = "INSERT INTO peeps_avg VALUES()"
    #c.execute(command) SEND HELP

command = """SELECT * FROM peeps_avg"""
c.execute (command)
for row in c:
    print (row)
