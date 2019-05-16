from threading import Thread
from SocketServer import ThreadingTCPServer,BaseRequestHandler
from dataAccess.getInputModule import LoadCaseData, BuildVesselTypeCollection
from tools.writeOutputModule import WriteKML

class DynamicDataHandler(BaseRequestHandler):

    def generateKML(self):
        f = WriteKML()
        kml = f.write()
        return kml    
    
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.request.recv(1024)
        self.data = self.generateKML()
        self.request.sendall(self.data)

class RunDynamicDataSercer(Thread):
    def __init__(self):
        LoadCaseData().load()
        BuildVesselTypeCollection().buildVesselTypeDict()
        Thread.__init__(self)
    def run(self):
        global mutex
        try:
            HOST, PORT = "localhost", 21578
            ThreadingTCPServer.allow_reuse_address = True
            server = ThreadingTCPServer((HOST, PORT), DynamicDataHandler)
            print "\n\rwaiting for dynamic data......"
            server.serve_forever()
            if mutex.acquire(1):
                mutex.release()
        except:
            if mutex.acquire(1):
                print "couldnot connect"
                mutex.release()

        
