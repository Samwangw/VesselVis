import core
import core.vesselModule
import os
import businessLogic
import dataServer

class WriteKML(object):
    '''
    classdocs
    '''
    def __init__(self):
        pass
    
    def buildKMLHead(self):
        if core.isHistory:
            styleOtherPath      = self.buildPathStyle("pn_Other",       "33ffffff",".2","ph_Other",         "ffffffff","3","mpn_Other")
            styleLawPath        = self.buildPathStyle("pn_Law",         "33ff5909",".2","ph_Law",           "ffff5909","3","mpn_Law")
            styleTugPath        = self.buildPathStyle("pn_Tug",         "33c70eff",".2","ph_Tug",           "ffc70eff","3","mpn_Tug")
            stylePleasurePath   = self.buildPathStyle("pn_Pleasure",    "3393ff01",".2","ph_Pleasure",      "ff93ff01","3","mpn_Pleasure")
            stylePortTenderPath = self.buildPathStyle("pn_PortTender",  "330da6ff",".2","ph_PortTender",    "ff0da6ff","3","mpn_PortTender")
            styeleCargoPath     = self.buildPathStyle("pn_Cargo",       "3302fcff",".2","ph_Cargo",         "ff02fcff","3","mpn_Cargo")
            styleUnknownPath    = self.buildPathStyle("pn_Unknown",     "331f0cff",".2","ph_Unknown",       "ff1f0cff","3","mpn_Unknown")
            
            styleOtherPoint     = self.buildPointStyle("sn_Other","0.02",       os.path.join(core.path,"test","ShipLogo","Other_dot.png"),      "ffffffff","0.4","sh_Other","0.8",      os.path.join(core.path,"test","ShipLogo","Other_dot.png"),"ffffffff","0.4","msn_Other")
            styleLawPoint       = self.buildPointStyle("sn_Law","0.02",         os.path.join(core.path,"test","ShipLogo","Navy_dot.png"),       "ffff5909","0.4","sh_Law","0.8",        os.path.join(core.path,"test","ShipLogo","Navy_dot.png"),"ffff5909","0.4","msn_Law")
            styleCargoPoint     = self.buildPointStyle("sn_Cargo","0.02",       os.path.join(core.path,"test","ShipLogo","Cargo_dot.png"),      "ff02fcff","0.4","sh_Cargo","0.8",      os.path.join(core.path,"test","ShipLogo","Cargo_dot.png"),"ff02fcff","0.4","msn_Cargo")
            styleTugPoint       = self.buildPointStyle("sn_Tug","0.02",         os.path.join(core.path,"test","ShipLogo","Tug_dot.png"),        "ffc70eff","0.4","sh_Tug","0.8",        os.path.join(core.path,"test","ShipLogo","Tug_dot.png"),"ffc70eff","0.4","msn_Tug")
            stylePleasurePoint  = self.buildPointStyle("sn_Pleasure","0.02",    os.path.join(core.path,"test","ShipLogo","Cruises_dot.png"),    "ff93ff01","0.4","sh_Pleasure","0.8",   os.path.join(core.path,"test","ShipLogo","Cruises_dot.png"),"ff93ff01","0.4","msn_Pleasure")
            stylePortTenderPoint= self.buildPointStyle("sn_PortTender","0.02",  os.path.join(core.path,"test","ShipLogo","PortTender_dot.png"), "ff0da6ff","0.4","sh_PortTender","0.8", os.path.join(core.path,"test","ShipLogo","PortTender_dot.png"),"ff0da6ff","0.4","msn_PortTender")
            styleUnknowPoint    = self.buildPointStyle("sn_Unknown","0.02",     os.path.join(core.path,"test","ShipLogo","Unknown_dot.png"),    "ff1f0cff","0.4","sh_Unknown","0.8",    os.path.join(core.path,"test","ShipLogo","Unknown_dot.png"),"ff1f0cff","0.4","msn_Unknown")
            styleAlertPoint     = ""
        
        else:
            styleOtherPath      = self.buildPathStyle("pn_Other",       "ffffffff","2","ph_Other",      "ffffffff","3","mpn_Other")
            styleLawPath        = self.buildPathStyle("pn_Law",         "ffff5909","2","ph_Law",        "ffff5909","3","mpn_Law")
            styeleCargoPath     = self.buildPathStyle("pn_Cargo",       "ff02fcff","2","ph_Cargo",      "ff02fcff","3","mpn_Cargo")
            styleTugPath        = self.buildPathStyle("pn_Tug",         "ffc70eff","2","ph_Tug",        "ffc70eff","3","mpn_Tug")
            stylePleasurePath   = self.buildPathStyle("pn_Pleasure",    "ff93ff01","2","ph_Pleasure",   "ff93ff01","3","mpn_Pleasure")
            stylePortTenderPath = self.buildPathStyle("pn_PortTender",  "ff0da6ff","2","ph_PortTender", "ff0da6ff","3","mpn_PortTender")
            styleUnknownPath    = self.buildPathStyle("pn_Unknown",     "ff1f0cff","2","ph_Unknown",    "ff1f0cff","3","mpn_Unknown")
            
            styleOtherPoint     = self.buildPointStyle("sn_Other","0.5",        os.path.join(core.path,"test","ShipLogo","Other.png"),      "ffffffff","0.4","sh_Other","0.8",      os.path.join(core.path,"test","ShipLogo","Other.png"),"ffffffff","0.4","msn_Other")
            styleLawPoint       = self.buildPointStyle("sn_Law","0.5",          os.path.join(core.path,"test","ShipLogo","Navy.png"),       "ffff5909","0.4","sh_Law","0.8",        os.path.join(core.path,"test","ShipLogo","Navy.png"),"ffff5909","0.4","msn_Law")
            styleCargoPoint     = self.buildPointStyle("sn_Cargo","0.5",        os.path.join(core.path,"test","ShipLogo","Cargo.png"),      "ff02fcff","0.4","sh_Cargo","0.8",      os.path.join(core.path,"test","ShipLogo","Cargo.png"),"ff02fcff","0.4","msn_Cargo")
            styleTugPoint       = self.buildPointStyle("sn_Tug","0.5",          os.path.join(core.path,"test","ShipLogo","Tug.png"),        "ffc70eff","0.4","sh_Tug","0.8",        os.path.join(core.path,"test","ShipLogo","Tug.png"),"ffc70eff","0.4","msn_Tug")
            stylePleasurePoint  = self.buildPointStyle("sn_Pleasure","0.5",     os.path.join(core.path,"test","ShipLogo","Cruises.png"),    "ff93ff01","0.4","sh_Pleasure","0.8",   os.path.join(core.path,"test","ShipLogo","Cruises.png"),"ff93ff01","0.4","msn_Pleasure")
            stylePortTenderPoint= self.buildPointStyle("sn_PortTender","0.5",   os.path.join(core.path,"test","ShipLogo","PortTender.png"), "ff0da6ff","0.4","sh_PortTender","0.8", os.path.join(core.path,"test","ShipLogo","PortTender.png"),"ff0da6ff","0.4","msn_PortTender")
            styleUnknowPoint    = self.buildPointStyle("sn_Unknown","0.5",      os.path.join(core.path,"test","ShipLogo","Unknown.png"),    "ff1f0cff","0.4","sh_Unknown","0.8",    os.path.join(core.path,"test","ShipLogo","Unknown.png"),"ff1f0cff","0.4","msn_Unknown")
            styleAlertPoint     = self.buildPointStyle("sn_Alert","0.8",        os.path.join(core.path,"test","ShipLogo","Circle.png"),     "ff1f0cff","0.4","sh_Alert","1",        os.path.join(core.path,"test","ShipLogo","Circle.png"),"ff1f0cff","0.4","msn_Alert")
             
        kmlhead = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                   '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n'
                   '<Folder>\n'
                   '<name>Defense Data Challenge</name>\n'
                   '<description>This is a case to show vessel real time data in sub-area of AU</description>\n'
                   )
        kmlhead += styleOtherPath;
        kmlhead += styeleCargoPath;
        kmlhead += styleUnknownPath;
        kmlhead += styleTugPath;
        kmlhead += stylePortTenderPath;
        kmlhead += stylePleasurePath;
        kmlhead += styleLawPath;
        
        kmlhead += styleOtherPoint;
        kmlhead += styleCargoPoint;
        kmlhead += styleUnknowPoint;
        kmlhead += styleTugPoint;
        kmlhead += stylePortTenderPoint;
        kmlhead += stylePleasurePoint;
        kmlhead += styleLawPoint;
        kmlhead += styleAlertPoint
        
        return kmlhead
    
    def buildKMLEnd(self):
        kmlend = ('</Folder>\n'
                 '</kml>\n')
        return kmlend
    
    def write(self):
        #write the KML Head
        countVessel = 0;
        
        outkml = self.buildKMLHead()
  
        for k,v in core.vessels.getVessels().items():
            '''
            If it is the selected vessel, load location points
            '''
            if countVessel<1600:
                intstamp = v.getRecords()[v.startrecord].INTSTAMP
                if (intstamp>= core.startime) and (intstamp < core.startime + core.dynamicInterval):
                    innerPath = ('<Placemark>\n'
                       '<name>%s</name>\n'
                       '<visibility>1</visibility>\n')%(k)
                    innerPath += self.getPathStyleURLbyVesselType(v.getRecords()[0].TYPE)
                    innerPath += ('<LineString>\n'
                       '<tessellate>100</tessellate>\n'
                       '<coordinates>\n')
                    for x in range(v.startrecord,len(v.getRecords())):
                        r = v.getRecords()[x]
                        if r.INTSTAMP > core.startime + core.dynamicInterval:
                            break
                        txtr = r.LON + "," + r.LAT + ",0 "
                        innerPath += txtr
                        v.startrecord = x
                    innerPath += ('</coordinates>\n'
                                '</LineString>\n'
                                '</Placemark>\n')
                    outkml += innerPath
                    innerPlace = ('<Placemark>\n'
                                  '<name>%s</name>\n')%(k)
                    innerPlace+= self.getPointStylebyVesselType(v.getRecords()[0].TYPE)
                    #innerPlace += self.VesselTypeURL(VesselType)
                    innerPlace += ('<Style>\n'
                                '<IconStyle>\n'
                                '<heading>%s</heading>\n'
                                '</IconStyle>\n'
                                '</Style>\n'
                                '<Point>\n'
                                '<gx:drawOrder>1</gx:drawOrder>\n'
                                '<coordinates>%s,%s,0</coordinates>\n'
                                '</Point>\n'
                                '</Placemark>\n')%(v.getRecords()[v.startrecord].COURSE, v.getRecords()[v.startrecord].LON, v.getRecords()[v.startrecord].LAT)
                    outkml += innerPlace
            else :
                break
        core.startime += core.dynamicInterval/2
        if core.startime > core.maxtime:
            core.startime = core.mintime
            for v in core.vessels.getVessels().values():
                v.startrecord = 0;
        pass
        
        outkml += self.buildKMLEnd()

        return outkml

    def writeHisPath(self):
        print "...HisPath kml begin..."
        if os.path.isfile(core.hisfile):
            os.remove(core.hisfile)
        outkml = self.buildKMLHead()
        f=open(core.hisfile,'a')
        f.write(outkml)
        #drawtype = "path"
        drawtype = self.getHisType()
        index = 0
        for k,v in core.vesselGroups.items():
            index += 1
            f.write('<Folder>\n<name>')
            f.write(str(k))
            f.write('</name>\n')
            for vid in v:
                vessel = core.vessels.getVessels()[vid]
                if vessel.getRecords()[0].TYPE=="":
                    continue
                if drawtype == "path":
                    innerPath = ('<Placemark>\n'
                               '<name>%s</name>\n'
                               '<visibility>1</visibility>\n')%(vid)
                    innerPath += self.getPathStyleURLbyVesselType(vessel.getRecords()[0].TYPE)
                    innerPath += ('<LineString>\n'
                                   '<tessellate>100</tessellate>\n'
                                   '<coordinates>\n')
                    for x in range(vessel.startrecord,len(vessel.getRecords())):
                        r = vessel.getRecords()[x]
                        txtr = r.LON + "," + r.LAT + ",0 "
                        innerPath += txtr
                    innerPath += ('</coordinates>\n'
                                    '</LineString>\n'
                                    '</Placemark>\n')
                    f.write(innerPath)
                    
                if drawtype == "point":
                    for x in range(vessel.startrecord,len(vessel.getRecords())):
                        r = vessel.getRecords()[x]
                        innerPoint = r'<Placemark>'+self.getPointStylebyVesselType(vessel.getRecords()[0].TYPE)+'<Point><coordinates>'+r.LON + "," + r.LAT + ",0 "+ r'</coordinates></Point></Placemark>\n'
                        f.write(innerPoint)
                index += 1
                print index,"vessel finished."
            f.write('</Folder>')
            
        outkml = self.buildKMLEnd()
        f.write(outkml)
        print "...response kml end..."
        f.close()    

        #return outkml
    
    def wirteTarget(self):
        #write the KML Head
        countVessel = 0;
        
        outkml = self.buildKMLHead()
  
        for k,v in core.cloneVessels.getVessels().items():
            '''
            If it is the selected vessel, load location points
            '''
            if countVessel<1600:
                intstamp = v.getRecords()[v.startrecord].INTSTAMP
                if (intstamp>= core.startime) and (intstamp < core.startime + core.syntheInterval):
                    innerPath = ('<Placemark>\n'
                       '<name>%s</name>\n'
                       '<visibility>1</visibility>\n')%(k)
                    innerPath += ('<styleUrl>#mpn_Tug</styleUrl>\n'
                        '<LineString>\n'
                       '<tessellate>100</tessellate>\n'
                       '<coordinates>\n')
                    for x in range(v.startrecord,len(v.getRecords())):
                        r = v.getRecords()[x]
                        if r.INTSTAMP > core.startime + core.syntheInterval:
                            break
                        txtr = r.LON + "," + r.LAT + ",0 "
                        innerPath += txtr
                        v.startrecord = x
                    innerPath += ('</coordinates>\n'
                                '</LineString>\n'
                                '</Placemark>\n')
                    outkml += innerPath
                    innerPlace = ('<Placemark>\n'
                                  '<name>%s</name>\n')%(k)

                    innerPlace += ('<styleUrl>#msn_Circle</styleUrl>\n'
                                '<Style>\n'
                                '<IconStyle>\n'
                                '<heading>%s</heading>\n'
                                '</IconStyle>\n'
                                '</Style>\n'
                                '<Point>\n'
                                '<gx:drawOrder>1</gx:drawOrder>\n'
                                '<coordinates>%s,%s,0</coordinates>\n'
                                '</Point>\n'
                                '</Placemark>\n')%(v.getRecords()[v.startrecord].COURSE, v.getRecords()[v.startrecord].LON, v.getRecords()[v.startrecord].LAT)
                    #print "time:",v.getRecords()[v.startrecord].INTSTAMP,"  lon:",v.getRecords()[v.startrecord].LON,"lat:",v.getRecords()[v.startrecord].LAT
                    outkml += innerPlace
                    if v.sTag:
                        innerS = ('<Placemark>\n'
                                '<styleUrl>#msn_Alert</styleUrl>\n'
                                '<Point>\n'
                                '<gx:drawOrder>1</gx:drawOrder>'
                                '<coordinates>%s,%s,0</coordinates>\n'
                                '</Point>\n'
                                '</Placemark>\n')%(v.getRecords()[v.startrecord].LON, v.getRecords()[v.startrecord].LAT)
                        outkml += innerS
            else :
                break
        core.startime += core.syntheInterval/2
        if core.startime >= core.mintime+200000:
            core.startime = core.mintime
            for v in core.cloneVessels.getVessels().values():
                v.startrecord = 0;
                v.sTag = False
        pass
        
        outkml += self.buildKMLEnd()

        return outkml

    '''
    To add different StypeURL for diverse vessels
    '''
    def getPathStyleURLbyVesselType(self, VesselType):
        if VesselType == "":
            kml = '<styleUrl>#mpn_Unknown</styleUrl>\n'
        elif VesselType.startswith("Cargo"):
            kml = '<styleUrl>#mpn_Cargo</styleUrl>\n'
        elif VesselType.startswith("Law"):
            kml = '<styleUrl>#mpn_Law</styleUrl>\n'
        elif VesselType.startswith("Tug"):
            kml = '<styleUrl>#mpn_Tug</styleUrl>\n'
        elif VesselType.startswith("Pleasure"):
            kml = '<styleUrl>#mpn_Pleasure</styleUrl>\n'
        elif VesselType.startswith("Port tender"):
            kml = '<styleUrl>#mpn_PortTender</styleUrl>\n'
        else:
            kml = '<styleUrl>#mpn_Other</styleUrl>\n'
        return kml
    
    def getPointStylebyVesselType(self,VesselType):
        if VesselType == "":
            kml = '<styleUrl>#msn_Unknown</styleUrl>\n'
        elif VesselType.startswith("Pleasure"):
            kml = '<styleUrl>#msn_Pleasure</styleUrl>\n'
        elif VesselType.startswith("Law"):
            kml = '<styleUrl>#msn_Law</styleUrl>\n'
        elif VesselType.startswith("Cargo"):
            kml = '<styleUrl>#msn_Cargo</styleUrl>\n'
        elif VesselType.startswith("Tug"):
            kml = '<styleUrl>#msn_Tug</styleUrl>\n'
        elif VesselType.startswith("Port tender"):
            kml = '<styleUrl>#msn_PortTender</styleUrl>\n'
        else:
            kml = '<styleUrl>#msn_Other</styleUrl>\n'
        return kml
    
    def buildPathStyle(self,nname,color1,width1,hname,color2,width2,mname):
        style =  '<Style id="'+nname+'">\n'+'<LineStyle>\n'+'<color>'+color1+'</color>\n'+'<width>'+width1+'</width>\n'+'</LineStyle>\n'+'</Style>\n'
        style += '<Style id="'+hname+'">\n'+'<LineStyle>\n'+'<color>'+color2+'</color>\n'+'<width>'+width2+'</width>\n'+'</LineStyle>\n'+'</Style>\n'
        style += '<StyleMap id="'+mname+'">\n<Pair>\n<key>normal</key>\n<styleUrl>#'+nname+'</styleUrl>\n</Pair>\n<Pair>\n<key>highlight</key>\n<styleUrl>#'+hname+'</styleUrl>\n</Pair>\n</StyleMap>\n'
        return str(style)
    def buildPointStyle(self,nname,scale1,path1,color1,lscale1,hname,scale2,path2,color2,lscale2,mname):
        style  = '<Style id="'+nname+'">\n<IconStyle>\n<scale>'+scale1+'</scale>\n<Icon>\n<href>'+path1+'</href>\n</Icon>\n</IconStyle>\n<LabelStyle>\n<color>'+color1+'</color>\n<colorMode>random</colorMode>\n<scale>'+lscale1+'</scale>\n</LabelStyle>\n</Style>\n'
        style += '<Style id="'+hname+'">\n<IconStyle>\n<scale>'+scale2+'</scale>\n<Icon>\n<href>'+path2+'</href>\n</Icon>\n</IconStyle>\n<LabelStyle>\n<color>'+color2+'</color>\n<colorMode>random</colorMode>\n<scale>'+lscale2+'</scale>\n</LabelStyle>\n</Style>\n'
        style += '<StyleMap id="'+mname+'">\n<Pair>\n<key>normal</key>\n<styleUrl>#'+nname+'</styleUrl>\n</Pair>\n<Pair>\n<key>highlight</key>\n<styleUrl>#'+hname+'</styleUrl>\n</Pair>\n</StyleMap>\n'
        return str(style)
    def getHisType(self):
        if core.histype == None:
            return "path"
        elif core.histype == "point":
            return "point"
        else:
            return "path"