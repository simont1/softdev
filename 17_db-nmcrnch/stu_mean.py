#Box3 Anton Danylenko, Simon Tsui
#SoftDev1 pd8
#K17 -- average
#2018-10-09T
import sqlite3
import csv
import db_builder


db_builder.main()
DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()


def name_to_ID(name):
    command = """SELECT name, id FROM roster"""
    c.execute(command)
    for row in c:
        if name == row[0]:
            return row[0]

def stu_name():
    command = """SELECT name, id FROM roster"""
    c.execute(command)
    return c.fetchall()
#print(stu_name())


#Prints out course grades per student via matching roster.id to courses.id
def grades():
    grades_str = ""
    command = """SELECT name, mark
    FROM roster, courses
    WHERE courses.id = roster.id"""
    c.execute(command)
    for row in c:
        grades_str += row[0] + " "  + str(row[1]) + " " +  "\n"
    return grades_str
print(grades())

#Prins out averages by student names and their averages

def avgs_make():
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
    return avgs
print (avgs_make())

def peeps_table():
    command = """CREATE TABLE peeps_avg(id INTEGER, avgs INTEGER)"""
    students = stu_name()
    c.execute(command)
    avgsList = avgs_make()
    for person in students:
        avgs = avgsList[person[0]]
        id = person[1]
        command = "INSERT INTO peeps_avg VALUES({},{})".format(id, avgs)
        c.execute(command)

peeps_table()
# db.commit()
# command = """SELECT * FROM peeps_avg"""
# c.execute (command)
# for row in c:
#     print (row)

def add_Row():
    code = 'code'
    #command = "INSERT INTO courses (code, mark, id) VALUES(code, 100, 90);"
    c.execute(command)

add_Row()
db.commit()
command = """SELECT * FROM courses"""
c.execute (command)
for row in c:
    print (row)
