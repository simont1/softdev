# azrael - Jason Tung and Simon Tsui
# SoftDev1 pd8
# K06 -- StI/O: Divine your Destiny!
# 2018-09-13
import csv
import random

def convert(filename):
    '''converts a two column csv file with table headers and footers into a key value pair dictionary'''
    #open file and parse it into a generator using csv reader
    #convert the generator into a list exluding the job and percentage table headers and footers
    #read values two at a time as tuples and use those to create a key value pair
    f = {k:float(v) for k,v in list(csv.reader(open(filename)))[1:-1]}
    return f

def pickRandom(f):
    '''takes a dictionary of key value pairs and returns a random key using the values as the percent chance of selecting the corresponding key'''
    #pick a number, any number (as long as it's an element of [0,99.8))
    rand = random.uniform(0, 99.8)
    #go through key value pairs in f
    for k,v in f.items():
        rand -= v
        #when the cumulative total is greater than the random value, return that key
        if rand <= 0:
            return k
    print("uh oh... something has gone awry!")

def main():
    f = convert("occupations.csv")
    print("appropriate dictionary: ", f)
    # print(reduce(lambda x,y: x+y, ([v for k,v in f.items()])))
    print("weighted random pick: ", pickRandom(f))
    print("--testing--")
    test()

def test():
    f = convert("occupations.csv")
    g = {k:0 for k in f}
    for x in range(10000):
        g[pickRandom(f)]+=1
    h = {k: v/100. for k,v in g.items()}
    print("generated dictionary from my weighted avg code: ", h)
    bool = True
    for k in h:
        if (f[k] - h[k])/f[k] >= .2:
            bool = False
    print("meets 20% margin for error" if bool else "does not meet 20% margin for error")

main()