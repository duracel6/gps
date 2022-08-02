import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from lettura_file import scale_to_img

data = {}
h_w=[731,475]

data={"LATITUDE":lats,"LONGITUDE" :[16.0,16.0]}

gps_data = tuple(zip(data['LATITUDE'], data['LONGITUDE']))

image = Image.open('map.png', 'r')  # Load map image.
img_points = []
for d in gps_data:
    x1, y1 = scale_to_img(d, (image.size[0], image.size[1]))  # Convert GPS coordinates to image coordinates.
    img_points.append((x1, y1))
draw = ImageDraw.Draw(image)
draw.line(img_points, fill=(255, 0, 0), width=2)  # Draw converted records to the map image.
image.show()

