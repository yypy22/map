import geopandas as gpd
import matplotlib.pyplot as plt
import geoplot as gplt
import json
from urllib.request import urlopen
from pandas_geojson import read_geojson_url
import geoplot.crs as gcrs
import numpy as np
import pandas as pd
#data is from this https://gadm.org/download_country.html
jpn = "/home/csimage/Desktop/gsoc/map/gadm41_JPN.gpkg"
map = gpd.read_file(jpn,layer=1)
map = map.loc[:,["NAME_1", "geometry"]]
# fig, ax = plt.subplots(figsize=(10, 10))
# map.plot(ax=ax, color='red', edgecolor='green')
#plt.show()

popu = pd.read_html("https://en.wikipedia.org/wiki/List_of_Japanese_prefectures_by_population")
popu = popu[1]
now = popu.iloc[:,[1,5]]
now.drop(47, inplace=True)
# print(now)
now["Prefectures"]=now["Prefectures"].str.replace("-to","")
now["Prefectures"]=now["Prefectures"].str.replace("-ken","")
now["Prefectures"]=now["Prefectures"].str.replace("-fu","")
now["Prefectures"]=now["Prefectures"].str.replace("Ō","O")
now["Prefectures"]=now["Prefectures"].str.replace("ō","o")
now = now.rename(columns={"Prefectures":"NAME_1"})
merged = pd.merge(map,now)
merged.plot(column="Census Population Oct 1, 2020",cmap="Spectral")

fig,ax = plt.subplots(figsize=(30,30))
bar = plt.cm.ScalarMappable(cmap="Spectral")
fig.colorbar(bar, label="Population")

plt.show()