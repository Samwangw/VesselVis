from tools.readFileModule import ReadSHP
from tools.readFileModule import ReadSHPList
import core

class LoadCaseData(object):
    def __init__(self):
        print "Loading Case Data"
        pass
    
    def load(self):
        loader = ReadSHPList()
        loader.read(core.casepath)
        
class LoadHistoryData(object):
    def __init__(self):
        print "Loading History Data"
        pass
    
    def load(self):
        loader = ReadSHPList()
        loader.read(core.hispath)
        print "...",core.vessels.count(),"vessels data are loaded."
class BuildVesselTypeCollection(object):
    def __init__(self):
        pass
    def buildVesselTypeDict(self):
        for v in core.vessels.getVessels().values():
            core.vesselTypes.addType(v.type)
        for t in core.vesselTypes.getTypes():
            core.vesselGroups[t]=list()
        for v in core.vessels.getVessels().values():
            core.vesselGroups[v.type].append(v.CRAFT_ID)
    