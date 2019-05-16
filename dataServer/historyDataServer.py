from threading import Thread
from SocketServer import ThreadingTCPServer,BaseRequestHandler
from dataAccess.getInputModule import LoadHistoryData, BuildVesselTypeCollection
from tools.writeOutputModule import WriteKML

class HistoryDataHandler(BaseRequestHandler):

    def generateKML(self):
        pass  
    
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.request.recv(1024).strip()
        self.data = self.generateKML()
        self.request.sendall(self.data)

class RunHistoryDataSercer(Thread):
    def __init__(self):
        LoadHistoryData().load()
        BuildVesselTypeCollection().buildVesselTypeDict()
        WriteKML().writeHisPath()
        Thread.__init__(self)
    def run(self):
        global mutex
        try:
            HOST, PORT = "localhost", 21577
            ThreadingTCPServer.allow_reuse_address = True
            server = ThreadingTCPServer((HOST, PORT), HistoryDataHandler)
            print "\n\rwaiting for history data......"
            server.serve_forever()
            if mutex.acquire(1):
                mutex.release()
        except:
            if mutex.acquire(1):
                print "couldnot connect"
                mutex.release()