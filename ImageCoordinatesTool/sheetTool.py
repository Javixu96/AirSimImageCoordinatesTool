import uno
import utm

def getLibreOfficeConnection():
    localContext = uno.getComponentContext()

    resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext )

    ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext( "com.sun.star.frame.Desktop",ctx)
    model = desktop.getCurrentComponent()

    active_sheet = model.CurrentController.ActiveSheet

    return active_sheet

def fillSheetWithCoordinates(active_sheet,columnPosX,Row,columnLat):
    
    while active_sheet.getCellByPosition(columnPosX,Row).Value != 0:

        XmE = active_sheet.getCellByPosition(columnPosX,Row).Value
        YmN = active_sheet.getCellByPosition(columnPosX+1,Row).Value

        LatLong=utm.to_latlon(XmE, YmN, 30, 'T')

        active_sheet.getCellByPosition(columnLat,Row).Value = LatLong[0]
        active_sheet.getCellByPosition(columnLat+1,Row).Value = LatLong[1]
        Row+=1

