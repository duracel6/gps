import re
import pandas
import numpy
from turtle import color
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import PIL

points=(40.7763,14.7248,40.6924,14.8964)

def scale_to_img(lat_lon, h_w):
    """
    Conversion from latitude and longitude to the image pixels.
    It is used for drawing the GPS records on the map image.
    :param lat_lon: GPS record to draw (lat1, lon1).
    :param h_w: Size of the map image (w, h).
    :return: Tuple containing x and y coordinates to draw on map image.
    """
    # https://gamedev.stackexchange.com/questions/33441/how-to-convert-a-number-from-one-min-max-set-to-another-min-max-set/33445
    old = (points[2], points[0])
    new = (0, h_w[1])
    y = ((lat_lon[0] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
    old = (points[1], points[3])
    new = (0, h_w[0])
    x = ((lat_lon[1] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
    # y must be reversed because the orientation of the image in the matplotlib.
    # image - (0, 0) in upper left corner; coordinate system - (0, 0) in lower left corner
    return int(x), h_w[1] - int(y)

lats=[]
lons=[]
writingFile = open(r"C:\Users\ccliu\Desktop\gps\log.txt",mode='w') #apertura e creazione file di scrittura
with  open(r"C:\Users\ccliu\Desktop\gps\ciao.log")  as readingFile: #apertura Log 
    for line in readingFile:
        x=re.search("^\\$xxRMC floating point degree coordinates and speed:",line)
        #print(line,"ciao")
        if (x):
            lat=line.split(":")[1].split(" ")[1].split("(")[1].split(",")[0]
            long=line.split(":")[1].split(" ")[1].split(")")[0].split(",")[1]
            #print(lat,long)
            lats.append(float(lat))
            lons.append(float(long))
            writingFile.write( lat + "," + long +"\n")
data={"LATITUDE":lats,"LONGITUDE" :lons}          
gps_data = tuple(zip(data['LATITUDE'], data['LONGITUDE']))
image = Image.open(r"C:\Users\ccliu\Desktop\gps\map (2).png", 'r')  # Load map image.
img_points = []
for d in gps_data:
    x1, y1 = scale_to_img(d, (image.size[0], image.size[1]))  # Convert GPS coordinates to image coordinates.
    img_points.append((x1, y1))
draw = ImageDraw.Draw(image)
draw.line(img_points, fill=(255, 0, 0), width=2)  # Draw converted records to the map image.
image.show()
plt.scatter(lats, lons)
plt.show()
writingFile.close()
