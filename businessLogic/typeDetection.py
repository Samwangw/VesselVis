import core
import math
import dis

class Detection(object):
    def __init__(self):
        pass
    def detect(self):
        for targetV in core.cloneVessels.getVessels().values():
            if targetV.sTag:
                continue
            x = targetV.getRecords()[targetV.startrecord].LAT
            y = targetV.getRecords()[targetV.startrecord].LON
            
            mindis = 99999.0
            for sourceV in core.vessels.getVessels().values():
                if sourceV.type == targetV.type:
                    for x in range(0,len(sourceV.getRecords())):
                        r = sourceV.getRecords()[x]
                        x1 = r.LAT
                        y1 = r.LON
                        dis = math.sqrt((float(x1)-float(x))*(float(x1)-float(x))+(float(y1)-float(y))*(float(y1)-float(y)))
                        #print dis
                        if dis < mindis:
                            mindis = dis
            
            if mindis > 20.55 and mindis< 150:
                targetV.sTag = True   
                
    
                
                
            
            
        