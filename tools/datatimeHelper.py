import time
import datetime

class DateTimeHelper(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    def getStampbyStr(self,strtime):
        timeArray = time.strptime(strtime, "%Y-%m-%dT%H:%M:%SZ")
        t = time.mktime(timeArray)
        timeStamp = int(t)
        return timeStamp
    '''
    To format the Time into specified format
    '''
    def TimeFormat(self, longdate):
        longdatearray = longdate.split(' ') 
        if len(longdatearray)>0:
            date = longdatearray[0]
            datearrary = date.split('/')
            day = datearrary[0]
            month = datearrary[1]
            year = datearrary[2]
            date = year + "-" + month + "-" + day
            
            if len(longdatearray)>1:
                time = longdatearray[1]
                timearray = time.split(':')
                hour = timearray[0]
                min = timearray[1]
                sec = timearray[2]
                if longdatearray[2] == "AM" and timearray[0] == "12":
                    hour = 0
                if longdatearray[2] == "PM":
                    hour = int(timearray[0])+12
                if hour == 24:
                    hour = 0
                time = str(hour) + ":" + min + ":" + sec
            else:
                time = "00:00:00"
            
            finaldate = date + "T" + time + "Z"
        return finaldate