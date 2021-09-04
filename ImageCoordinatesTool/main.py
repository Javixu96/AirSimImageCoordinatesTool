import uno
import sheetTool
import imageTool

def main():

    sheet = sheetTool.getLibreOfficeConnection()
    
    inicialRow = 1
    columnPosX = 5
    columnLat = 7
    columnHigh = 4

    sheetTool.fillSheetWithCoordinates(sheet,columnPosX,inicialRow,columnLat)

    originFolder = "/home/example/pngFolder"
    destinationFolder = "/home/example/jpgFolder"
    
    imageTool.convertPngToJpg(originFolder,destinationFolder)
    
    imageTool.insertCoordinatesInJpgExif(sheet,inicialRow,columnLat,columnHigh,destinationFolder)
  
main()