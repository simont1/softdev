#Simon Tsui 
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

with open('peeps.csv') as csvfile:
    command = "CREATE TABLE roster (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)"        #build SQL stmt, save as string
    c.execute(command)    #run SQL statement

    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO roster (name, age, id) VALUES('" +row['name']+"','"+row['age']+"','"+row['id']+"');")

#c.execute("SELECT * FROM roster;")
#print( c.fetchall())

with open('courses.csv') as csvfile:
    command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"        #build SQL stmt, save as string
    c.execute(command)    #run SQL statement
    reader = csv.DictReader(csvfile)
    for row in reader:
           c.execute("INSERT INTO courses (code, mark, id) VALUES('" +row['code']+"','"+row['mark']+"','"+row['id']+"');")

#==========================================================

db.commit() #save changes
db.close()  #close database
