import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium import Choropleth, Circle, Marker,IFrame,CircleMarker
from folium.plugins import HeatMap, MarkerCluster 
import math
import json

data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-22-2020.csv')
print(data['Province/State'])
#Country/Region,Province/State,Confirmed,Deaths,Recovered,Latitude,Longitude
m_3 = folium.Map(location=[20.5937,78.9629], tiles='CartoDB dark_matter', zoom_start=2)
#data['Confirmed']
fg=folium.FeatureGroup(name='Marker', show=True)
m_3.add_child(fg)
fg1=folium.FeatureGroup(name='Circle', show=True)
m_3.add_child(fg1)
mc = MarkerCluster().add_to(fg)
mc1=MarkerCluster().add_to(fg1)
for idx, row in data.iterrows():
    if (str(row['Province/State'])!="nan"):
            location=[row['Latitude'],row['Longitude']]
            popup='<div style="width:300">'+'<STRONG>'+'<h3>'+str(row['Province/State'])+'</h3>'+'<br>'+'<p>'+'Confirmed-'+str(row['Confirmed'])+'<br>'+'Deaths-'+str(row['Deaths'])+'<br>'+'Recovered-'+str(row['Recovered'])+'</p>'+'</STRONG>'+'</div>'
            mc.add_child(Marker(location=location,popup=popup,icon=folium.Icon(color='red', icon='info-sign')))
            radius=15000 + int(row['Confirmed']) * 20
            mc1.add_child(Circle(location=location,popup=popup,radius=radius,fill_colour='#FF0000',color="red",fill=True))
    else:
        location=[row['Latitude'],row['Longitude']]
        popup='<div style="width:300">'+'<STRONG>'+'<h3>'+row['Country/Region']+'</h3>'+'<br>'+'<p>'+'Confirmed-'+str(row['Confirmed'])+'<br>'+'Deaths-'+str(row['Deaths'])+'<br>'+'Recovered-'+str(row['Recovered'])+'</p>'+'</STRONG>'+'</div>'
        mc.add_child(Marker(location=location,popup=popup,icon=folium.Icon(color='red', icon='info-sign')))    
        radius=15000 + int(row['Confirmed']) * 20
        mc1.add_child(Circle(location=location,popup=popup,radius=radius,fill_colour='#FF0000',color="red",fill=True))

folium.LayerControl().add_to(m_3)
m_3.save("../index.html")
m_3