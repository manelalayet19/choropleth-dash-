from urllib.request import urlopen
import plotly.offline as offline
import geojson
import pandas as pd
import plotly 
import plotly as plt
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
                        #chartstudio for data less than 524KO #
# import chart_studio 
# import chart_studio.plotly as py
# chart_studio.tools.set_credentials_file(username='manelalayet',api_key='jo6DzgbxCDZ19jcD66RU') 
                    #define data frame using pandas lib and display data for population in Tunisia 
df = pd.read_csv("py/tngov -1.csv")
print(df)
                            #Geojson data from url source 
with urlopen('http://www.openculture.gov.tn/dataset/70fd9b49-3925-477f-ae17-9d206d650aab/resource/4b3d85dd-a523-425c-b477-ab9fec6e51a0/download/decoupage.geojson') as response:
    cities = geojson.load(response)
print(cities['features'][0])

                                    #choropleth map
fig= px.choropleth_mapbox(df, geojson=cities,locations='id', color='population ', 
color_continuous_scale="Viridis",hover_name = 'deleg_na_1', hover_data =["gov_name_f","gov_id","population "],
labels={'population':'population number'}, mapbox_style="carto-darkmatter",zoom=4,
center = {"lat": 36.82189, "lon":10.168969 })
#py.plot(fig,filename='choropleth', open_auto=True)
fig.show()
#                                             #set data 2 
# df_product_viande= pd.read_csv('Production totale du viande par type.csv')
# #print(df_product_viande)
# fig2 = px.line(df_product_viande, x = df_product_viande['id'], y =df_product_viande==['2017'],
# title='Production totale du viande')
# data= [fig, fig2]


plt.offline.plot(fig, filename = 'map.html')
