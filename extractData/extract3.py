import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium import Choropleth, Circle, Marker,IFrame
from folium.plugins import HeatMap, MarkerCluster
import math
import json

data = pd.read_csv('../Data/coronadata.csv')
print(data['Province/State'])
#Country/Region,Province/State,Confirmed,Deaths,Recovered,Latitude,Longitude
m_3 = folium.Map(location=[20.5937,78.9629], tiles='cartodbpositron', zoom_start=2)
data['Confirmed']
mc = MarkerCluster()
for idx, row in data.iterrows():
    coords,popups=[],[]
    if (str(row['Province/State'])!="nan"):
            location=[row['Latitude'],row['Longitude']]
            popup='<STRONG>'+'<h3>'+str(row['Province/State'])+'</h3>'+'<br>'+'<p>'+'Confirmed-'+str(row['Confirmed'])+'<br>'+'Deaths-'+str(row['Deaths'])+'<br>'+'Recovered-'+str(row['Recovered'])+'</p>'+'</STRONG>'
            mc.add_child(Marker(location=location,popup=popup))
    else:
        location=[row['Latitude'],row['Longitude']]
        popup='<STRONG>'+'<h3>'+row['Country/Region']+'</h3>'+'<br>'+'<p>'+'Confirmed-'+str(row['Confirmed'])+'<br>'+'Deaths-'+str(row['Deaths'])+'<br>'+'Recovered-'+str(row['Recovered'])+'</p>'+'</STRONG>'
        mc.add_child(Marker(location=location,popup=popup))    
        

m_3.add_child(mc)
m_3.save("../index.html")
m_3