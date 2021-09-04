# ImageGPSTool
Image GPS tool: convert png to jpg, convert UTM, insert coordinates information to jpg 

## How to use

### what is needed 

- A folder with .png photos, to ensure order, rename them to 1.png, 2.png .... (Select all -> rename) 
- A AirSim self-generated image recording information .txt file, like this:

![](https://github.com/Javixu96/ImageCoordinatesTool/blob/main/self-generatedSheet.png)

> AirSim Self-generated .txt file.

### Get connection to LibreOffice Calc

> /usr/lib/libreoffice/program/soffice.bin --calc --accept="socket,host=localhost,port=2002;urp;"

And then open your .txt file with LibreOffice Calc.

### Fields to fill in main.py

- inicialRow, the first row with values, normally with AirSim it is the second row (Value 1 in this case, since it starts with row 0). 
- columnPosX, int that indicates the column with UTM X position data (use the addition function to fill it: POS_X + origin point in UTM system position).
- columnLat, empty column use to save latitude, next column for longitude.
- columnHigh, the column with height information (Column "POX_Z" in self-generated file).
- originFolder, path to folder with .png images. 
- destinationFolder, path to the folder that you want to save the .jpg images.

### Example of how to prepare the sheet 

in main.py:

inicialRow = 1, columnPosX = 5, ColumnLat = 7 (Longitude = 8 ), columnHigh = 4.

![](https://github.com/Javixu96/ImageCoordinatesTool/blob/main/exampleSheet.png)

> Example of sheet format.

In this case, the origin point set in setting.json is 40.929144/-4.053847, after use conversor online to UTM system, the value is 411274.28m/4531426.01 in 30T zone, 
adds the values of column POS_X with 411274.28 to obtain columnPosX, and POS_Y with 4531426.01 for next column.

The UTM zone can be changed in sheetTool.py -> function "fillSheetWithCoordinates".


## Output

.jpg format images with its corresponding latitude and longitude saved in the destinationFolder:

![](https://github.com/Javixu96/ImageCoordinatesTool/blob/main/outputImage.png)

