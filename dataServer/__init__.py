from SocketServer import ThreadingTCPServer
from threading import Thread,activeCount,Lock
from dataServer.dynamicDataServer import RunDynamicDataSercer
from dataServer.syntheDataServer import RunSyntheDataSercer
from dataServer.historyDataServer import RunHistoryDataSercer
import core

mutex = Lock()

class MainThread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        if core.isDynamic:
            RunDynamicDataSercer().start()
        if core.isSynthe:
            RunSyntheDataSercer().start()
        if core.isHistory:
            RunHistoryDataSercer().start()
        self.outputInfo()
    def outputInfo(self):
        for t in core.vesselTypes.getTypes():
            print ">>",t,":",len(core.vesselGroups[t])," vessels" 