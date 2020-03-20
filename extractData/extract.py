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

variable='Cases'
vmin, vmax = 0, 80000

fig, ax = plt.subplots(1, figsize=(10, 6))

merged.plot(column=variable, cmap='BuGn', linewidth=0.5, ax=ax, edgecolor='0.5')
#plt.show()

# remove the axis
ax.axis("off")# add a title
ax.set_title("Covid-19-Confirmed Cases", fontdict={"fontsize": "25", "fontweight" : "3"})# create an annotation for the data source
ax.annotate("Source: European Centre for Disease Prevention and Control , 2020",xy=(0.1, .08), xycoords="figure fraction", horizontalalignment="left", verticalalignment="top", fontsize=12, color="#555555")

sm = plt.cm.ScalarMappable(cmap="BuGn", norm=plt.Normalize(vmin=vmin, vmax=vmax))# empty array for the data range
sm._A = []# add the colorbar to the figure
cbar = fig.colorbar(sm)#saving our map as .png file.
fig.savefig("map_export.png", dpi=300)

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