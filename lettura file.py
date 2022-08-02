import re
from turtle import color
import matplotlib.pyplot as plt
import geopandas 
apikey = ''
lats=[]
lons=[]
gmap = gmplot.GoogleMapPlotter(40.770732879,14.791375160, 14, apikey=apikey)

writingFile = open(r"C:\Users\ccliu\Desktop\loggps\log.txt",mode='w') #apertura e creazione file di scrittura
with  open(r"C:\Users\ccliu\Desktop\loggps\provafinale.txt")  as readingFile: #apertura Log 
    for line in readingFile:
        x=re.search("^\\$xxRMC floating point degree coordinates and speed:",line)
        #print(line,"ciao")
        if (x):
            lat=line.split(":")[1].split(" ")[1].split("(")[1].split(",")[0]
            long=line.split(":")[1].split(" ")[1].split(")")[0].split(",")[1]
            print(lat,long)
            lats.append(float(lat))
            lons.append(float(long))
            writingFile.write( lat + "," + long +"\n")
Università=lats,lons
gmap.paths(*Università,color='cornflowblue')
gmap.draw('map.html')

plt.plot(lats, lons)
plt.show()


writingFile.close()
