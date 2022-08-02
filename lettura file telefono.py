string1="dinates and speed"
import matplotlib.pyplot as plt
lats=[]
lons=[]

with open(r"C:\Users\ccliu\Desktop\loggps\prova2.txt") as readingFile: #apertura del file
  for line in readingFile:
    print(line)
    lat= line.split()[1].split(">")[0].split("=")[1]
    print(lat)
    lon= line.split()[2].split(">")[0].split("=")[1]
    lats.append(float(lat))
    lons.append(float(lon))


plt.plot(lats, lons)
plt.show()



