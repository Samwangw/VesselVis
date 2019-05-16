import os
from vesselModule import *

path = os.path.abspath('.')
#store data in these folders
casepath = os.path.join(path,"resources","shp")
hispath = os.path.join(path,"resources","HisShp")
isDynamic = False
isSynthe = True
isHistory = False
histype = "path"
hisfile = os.path.join(path,"test","his.kml")
dynamicInterval = 20000
syntheInterval = 15000
historynterval = 20000

mintime = 9999999999999999999   #min timestamp for all records
maxtime = 0                     #max timestamp for all records
startime = 0                    #start timestamp to generate KML

vessels = Vessels()
hisVessels = Vessels()
cloneVessels = Vessels()
vesselTypes = VesselTypes()
vesselGroups = dict()
