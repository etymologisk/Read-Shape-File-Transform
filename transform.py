from pyproj import Proj, transform
import geopandas as gpd
import pandas as pd

#read in shapefile
gc = gpd.read_file("Points.shp")

#convert lat/long to easting/northing in attribute table
p1 = Proj(init='epsg:4326')
p2 = Proj(init='epsg:32631')
E,N,Z = transform(p1, p2, gc['Longitude'].tolist(), gc['Latitude'].tolist(), [0] * len(gc.index) )

#convert from list to df
df = pd.DataFrame({'Easting1':E,'Northing1':N})

#add easting/northing to attibute table 
gc.join(df)

#export new shapefile
gc.to_file("Points2.shp")
