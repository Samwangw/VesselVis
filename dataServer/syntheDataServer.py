from threading import Thread
import random
import math
from SocketServer import ThreadingTCPServer,BaseRequestHandler
from tools.writeOutputModule import WriteKML
from dataAccess.getInputModule import LoadCaseData, BuildVesselTypeCollection
from businessLogic.typeDetection import Detection
import core

class SyntheDataHandler(BaseRequestHandler):

    def changeTrail(self):
        for v in core.cloneVessels.getVessels().values():
            x0 = float(v.getRecords()[0].LAT)
            y0 = float(v.getRecords()[0].LON)
            ran = random.random()
            x1 = -18.5*ran-12.0*(1-ran)
            y1 = 109.5*ran+120.5*(1-ran)
            tan = (x1-x0)/(y1-y0)
            parts = 100
            for x in range(0,parts):
                v.getRecords()[x].LAT = str(x0+(x1-x0)/float(parts)*x)
                v.getRecords()[x].LON = str(y0+(y1-y0)/float(parts)*x)
                v.getRecords()[x].INTSTAMP = core.startime + 2000*x
                v.getRecords()[x].COURSE = str(math.atan(tan)*180.0/math.pi)
                
    def generateKML(self):
        self.changeTrail()
        Detection().detect()
        WriteKML().wirteTarget()
        
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.request.recv(1024).strip()
        self.data = self.generateKML()
        self.request.sendall(self.data)

class RunSyntheDataSercer(Thread):
    def __init__(self):
        if len(core.vessels.getVessels())==0:
            print "No case data..."
            LoadCaseData().load()
            BuildVesselTypeCollection().buildVesselTypeDict()
        core.cloneVessels = self.generateTargets()
        Thread.__init__(self)
    def run(self):
        global mutex
        try:
            HOST, PORT = "localhost", 21579
            ThreadingTCPServer.allow_reuse_address = True
            server = ThreadingTCPServer((HOST, PORT), SyntheDataHandler)
            print "\n\rwaiting for synthesis data......"
            server.serve_forever()
            if mutex.acquire(1):
                mutex.release()
        except:
            if mutex.acquire(1):
                print "couldnot connect"
                mutex.release()
    def generateTargets(self):
        targets = core.vesselModule.Vessels()
        for v in core.vessels.getVessels().values():
            if len(v.getRecords())>350 and v.type == "Other":
                newV = v.clone()
                newV.type = "Tug"
                targets.addVessel(newV)
                break
        return targets
    