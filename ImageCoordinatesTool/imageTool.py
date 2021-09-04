from PIL import Image
from GPSPhoto import gpsphoto
import os

def convertPngToJpg(originFolder,destinationFolder):
      
   originList = os.listdir(originFolder)

   for x in range(len(originList)):
      fullPath=originFolder+"/"+str(x+1)+".png"
      img = Image.open(fullPath).convert("RGB")
      destinationPath=destinationFolder+"/"+str(x+1)+".jpg"
      img.save(destinationPath,optimize=False,format="jpeg",subsampling=0,quality=95)

def insertCoordinatesInJpgExif(active_sheet,Row,columnLat,columnHigh,destinationFolder): 

   destinationList=os.listdir(destinationFolder)

   for x in range(len(destinationList)):

      latitude = active_sheet.getCellByPosition(columnLat,Row).Value
      longitude = active_sheet.getCellByPosition(columnLat+1,Row).Value
      high = active_sheet.getCellByPosition(columnHigh,Row).Value
      high=round(high*-1)
      
      fullPath=destinationFolder+"/"+str(x+1)+".jpg"
      img = gpsphoto.GPSPhoto(fullPath)

      coordinates = gpsphoto.GPSInfo((latitude,longitude),alt=high)

      img.modGPSData(coordinates, fullPath)

      Row +=1






