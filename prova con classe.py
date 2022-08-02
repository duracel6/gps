

from gps_class import GPSVis

vis = GPSVis(data_path='log.cvs',
             map_path='map (4).png',  # Path to map downloaded from the OSM.
             points=(40.7794, 14.7701, 40.7602, 14.8115)) # Two coordinates of the map (upper left, lower right)

vis.create_image(color=(0, 0, 255), width=3)  # Set the color and the width of the GNSS tracks.
vis.plot_map(output='save')

print()