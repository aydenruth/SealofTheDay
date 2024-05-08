import datetime
import asyncio
import time
from scraper import getSeal

def getTime():
    now = datetime.datetime.now()

    now = str(now)
    currTime = now[11 : 16]
    
    return currTime

async def timer(length):
    length = int(length)
    while length > 0:
        asyncio.sleep(1)
        #it goes too fast from this figure out whats up n then u should be good
        #it might be 'break'ing at the timer call, allowing the loop to call it again and again (maybe crashing ur computer...)
        #if this is the case write a way to exit the loop and await responses while the timer is going 
        length -= 1
    print("All Done!")

#INITIALIZE:
desTime = "13:03"
isCont = True

#RUN:
def scheduler():
    while isCont:
        if desTime == getTime():
            print("match!")
            dailySeal = getSeal()
            print(dailySeal)
            #come back if ur 'losing time' from the code executing outside of the timer
            #and switch this to only post one time if the hour matches
            timer(3595)
            #count an hour from the exact time u want 2 post, minus 5 seconds to make up for code exucution 'lagging' the timer
            #call get imgs func

        elif desTime[3 : 5] == getTime()[3 : 5]:
            print("minuteMatch", desTime[3 : 5], getTime()[3 : 5])
            timer(3595)
            #once minutes match just need 2 count hourly
            #might have 2 adjust if time loss
        else:
            print("noMatch")
            timer(55)
            #if nothing matches check till the minutes do