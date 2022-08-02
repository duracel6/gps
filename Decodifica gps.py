from pynmeagps import NMEAReader
from asyncore import write
import re

from pyparsing import line_end
writingFile= open(r"C:\Users\ccliu\Desktop\loggps\decodificaNmea.txt",'w') 
with open(r"C:\Users\ccliu\Desktop\loggps\provaRaccoltaDati.txt") as readingFile: 
    for line in readingFile:
        try:
            msg=str(NMEAReader.parse(line))
    
            # print(msg)
            string = msg.split("(")[1].split(")")[0]
            print(string)
            writingFile.write(string+"\n")
        except:
            print("invalid string") 
writingFile.close()
writingFile = open(r"C:\Users\ccliu\Desktop\loggps\cordinateFinali.txt",'w')
with open(r"C:\Users\ccliu\Desktop\loggps\decodificaNmea.txt") as readingFile: 
    for line in readingFile:
        x=re.search("^GPRMC",line)
        if (x):
            time=line.split(", ")[1].split("=")[1]
            long=line.split(", ")[5].split("=")[1]
            lat=line.split(", ")[3].split("=")[1]
            writingFile.write(time + "," + lat + "," + long +"\n")
        else:
            print("no match")
writingFile.close()