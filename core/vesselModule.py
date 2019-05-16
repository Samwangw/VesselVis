'''
Created on 10/09/2015

@author: wwang1
'''
from tools.datatimeHelper import DateTimeHelper
import core

class Vessel(object):
    '''
    classdocs
    '''
    def __init__(self,vesselreord):
        if vesselreord != None:
            self.CRAFT_ID = vesselreord[0];
            self.records = list()
            self.type = VesselTypes().typeMapping(vesselreord[5])
            self.startrecord = 0
            self.sTag = False
        
    def addRecord(self,vesselrecord):
        self.records.append(VesselRecord(vesselrecord))
    def getRecords(self):
        return self.records
    def getCurrentLON(self):
        return self.getRecords()[len(self.getRecords())-1].LON
    def getCurrentLAT(self):
        return self.getRecords()[len(self.getRecords())-1].LAT
    def clone(self):
        newV = Vessel(None)
        newV.CRAFT_ID = self.CRAFT_ID
        newV.type = self.type
        newV.startrecord = 0
        newV.sTag = self.sTag
        newV.records = list()
        for r in self.getRecords():
            newR = VesselRecord(None)
            newR.CRAFT_ID = r.CRAFT_ID
            newR.LON =  r.LON
            newR.LAT = r.LAT
            newR.COURSE = r.COURSE
            newR.SPEED = r.SPEED
            newR.TYPE = r.TYPE 
            newR.SUBTYPE = r.SUBTYPE
            newR.LENGTH = r.LENGTH 
            newR.BEAM = r.BEAM
            newR.DRAUGHT = r.DRAUGHT
            newR.TIMESTAMP = r.TIMESTAMP
            newR.INTSTAMP = r.INTSTAMP
            newV.records.append(newR)
        return newV
            
        
        
class VesselRecord(object):
    def __init__(self,vesselreord):
        if vesselreord != None:
            self.CRAFT_ID = vesselreord[0];
            self.LON = vesselreord[1];
            self.LAT = vesselreord[2];
            self.COURSE = vesselreord[3];
            self.SPEED = vesselreord[4];
            self.TYPE = vesselreord[5]
            self.SUBTYPE = vesselreord[6];
            self.LENGTH =vesselreord[7];
            self.BEAM = vesselreord[8];
            self.DRAUGHT = vesselreord[9];
            self.TIMESTAMP = vesselreord[10];
            intstamp = DateTimeHelper().getStampbyStr(vesselreord[10])
            self.INTSTAMP = intstamp
            if intstamp < core.mintime:
                core.mintime = intstamp
                core.startime = intstamp
            if intstamp > core.maxtime:
                core.maxtime = intstamp
                
class Vessels:
        
    def __init__(self):
        self.__vesselsDic = dict()
        
    def addVessel(self, vessel):
        self.__vesselsDic[vessel.CRAFT_ID] = vessel
        
    def count(self):
        return len(self.__vesselsDic)
    
    def getVessels(self):
        return self.__vesselsDic

class VesselTypes:
    def __init__(self):
        self.__types = set()
    def isContain(self,type):
        if self.__types.get(type) == None:
            return False
        else:
            return True
    def addType(self,type):
            self.__types.add(type)
    def getTypes(self):
        return self.__types
    def typeMapping(self,str_type):
        if str_type == "":
            return "Unknown"
        elif str_type.startswith("Pleasure"):
            return "Pleasure"
        elif str_type.startswith("Law"):
            return "Law"
        elif str_type.startswith("Cargo"):
            return "Cargo"
        elif str_type.startswith("Tug"):
            return "Tug"
        elif str_type.startswith("Port tender"):
            return "PortTender"
        else:
            return "Other"