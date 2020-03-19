import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium import Choropleth, Circle, Marker,IFrame
from folium.plugins import HeatMap, MarkerCluster
import math
import json


country_geo = pd.read_csv('india-states.geo.csv')

data = pd.read_csv('data.csv')
data=data.rename(index=str,columns={"stateData": "province"})
df1 = pd.DataFrame(data,columns=['province', 'cases','deaths'])
df1.to_excel("output1.xlsx")
#print(df1)
merged = country_geo.merge(data, on='province') 
print(merged.head())

m_3 = folium.Map(location=[20.5937,78.9629], tiles='cartodbpositron', zoom_start=2)

mc = MarkerCluster()
for idx, row in merged.iterrows():
    if not math.isnan(row['cases']) and not math.isnan(row['cases']):
        location=[row['LAT'],row['LON']]
        popup='<STRONG>'+'State '+row['province']+'<br>'+'Cases-'+str(int((row['cases'])))+'<br>'+'Deaths-'+str(int((row['deaths'])))+'<br>'+'Discharged-'+str(int(row['discharged']))+'</STRONG>'
        mc.add_child(Marker(location=location,popup=popup))

m_3.add_child(mc)
m_3.save("./index1.html")
m_3
