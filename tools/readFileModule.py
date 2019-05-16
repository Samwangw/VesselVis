'''
Created on 10/09/2015

@author: wwang1
'''

import shapefile
import os
from core.vesselModule import *
import tools


class ReadSHP(object):
    def __init__(self):
        pass
    def read(self, path):
        sf = shapefile.Reader(path)
        records = sf.records()
        for r in records:
            vessel = core.vessels.getVessels().get(r[0])
            r[5] = r[5].strip()
            r[10] = tools.datatimeHelper.DateTimeHelper().TimeFormat(r[10])
            if vessel != None:
                vessel.addRecord(r)
            else:
                vessel = Vessel(r)
                vessel.addRecord(r)
                core.vessels.addVessel(vessel)
        
class ReadSHPList(object):
    def __init__(self):
        pass
    def read(self,path):
        fplist = self.getPathList(path)
        for fp in fplist:
            ReadSHP().read(fp)

    def getPathList(self, fullpath):
        fplist = list()
        filelist = os.listdir(fullpath)
        for v in filelist:
            if str(v).endswith(".dbf"):
                fplist.append(os.path.join(fullpath,v))
        return fplist
    pass        