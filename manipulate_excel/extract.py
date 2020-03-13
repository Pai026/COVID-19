import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# set the filepath and load
fp = "../world_border/countries.shp"
#reading the file stored in variable fp
map_df = gpd.read_file(fp)
# check data type so we can see that this is not a normal dataframe, but a GEOdataframe
map_df.head()
#map_df.plot()
#plt.show()

df = pd.read_excel (r'../pull-data/coronadata.xlsx')
df1=pd.DataFrame(df,columns=['Geold'])
print(df1)
df = pd.DataFrame(df, columns= ['CountryExp','NewConfCases','NewDeaths'])

aggregation_functions = {'NewConfCases': 'sum', 'NewDeaths': 'sum'}
df_new = df.groupby(df['CountryExp'],as_index=False).aggregate(aggregation_functions)
df_new=df_new.rename(index=str, columns={"CountryExp": "NAME"})
print(df_new)

df1 = pd.DataFrame(df_new,

                   columns=['CountryExp', 'NewConfCases'])

df1.to_excel("output.xlsx") 

df.head()

merged = map_df.merge(df_new, on='NAME', how='left')
print(merged.head())

variable='NewConfCases'
vmin, vmax = 0, 80000

fig, ax = plt.subplots(1, figsize=(10, 6))

merged.plot(column=variable, cmap='BuGn', linewidth=0.5, ax=ax, edgecolor='0.5')
plt.show()

# remove the axis
ax.axis("off")# add a title
ax.set_title("Covid-19-Confirmed Cases", fontdict={"fontsize": "25", "fontweight" : "3"})# create an annotation for the data source
ax.annotate("Source: European Centre for Disease Prevention and Control , 2020",xy=(0.1, .08), xycoords="figure fraction", horizontalalignment="left", verticalalignment="top", fontsize=12, color="#555555")

sm = plt.cm.ScalarMappable(cmap="BuGn", norm=plt.Normalize(vmin=vmin, vmax=vmax))# empty array for the data range
sm._A = []# add the colorbar to the figure
cbar = fig.colorbar(sm)#saving our map as .png file.
fig.savefig("map_export.png", dpi=300)

