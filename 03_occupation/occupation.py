#azrael - Simon Tsui, Jason Tung
#SoftDev1 pd8
#K06 -- StI/O: Divine your Destiny!
#2018-09-14F

import random
import reading


def rando():
    rolling_sum = random.randrange(998)
    for i in reading.total:
        rolling_sum -= reading.total[i] * 10
        if(rolling_sum < 0):
            return i

print(rando())
