import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium import Choropleth, Circle, Marker,IFrame
from folium.plugins import HeatMap, MarkerCluster
import math
import json


# set the filepath and load
fp = "/home/acer/Desktop/covid-19/world_border/TM_WORLD_BORDERS-0.3.shp"
#reading the file stored in variable fp
map_df = gpd.read_file(fp)
print(map_df['NAME'])
# check data type so we can see that this is not a normal dataframe, but a GEOdataframe
#map_df.head()

#map_df.plot()
#plt.show()

df = pd.read_excel (r'../Data/coronadata.xlsx')
df1=pd.DataFrame(df,columns=['Geold'])
print(df1)
df = pd.DataFrame(df, columns= ['Countries and territories','Cases','Deaths'])
print (df)
aggregation_functions = {'Cases': 'sum', 'Deaths': 'sum'}
df_new = df.groupby(df['Countries and territories'],as_index=False).aggregate(aggregation_functions)
df_new=df_new.rename(index=str, columns={"Countries and territories": "NAME"})
print(df_new)

df1 = pd.DataFrame(df_new,

                   columns=['NAME', 'Cases','Deaths'])

df1.to_excel("../Data/output.xlsx") 

#df.head()

merged = map_df.merge(df_new, on='NAME', how='left')
print(merged.head())



m_3 = folium.Map(location=[20.5937,78.9629], tiles='cartodbpositron', zoom_start=2)

mc = MarkerCluster()
for idx, row in merged.iterrows():
    coords,popups=[],[]
    if not math.isnan(row['Cases']) and not math.isnan(row['Cases']):
        location=[row['LAT'],row['LON']]
        popup='<STRONG>'+'Country '+row['NAME']+'<br>'+'Cases-'+str(int((row['Cases'])))+'<br>'+'Deaths-'+str(int((row['Deaths'])))+'</STRONG>'
        mc.add_child(Marker(location=location,popup=popup))
        
        

m_3.add_child(mc)
m_3.save("../index.html")
m_3