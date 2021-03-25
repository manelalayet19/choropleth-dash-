import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px 
import pandas as pd
import geojson
from urllib.request import urlopen
from dash.dependencies import Input, Output, State


app = dash.Dash()
colors= {
    'background':'#111111', 'text': '#FFFFFF', 'H1':'##143c24'
}
#define data frame using pandas lib and display data for population in Tunisia 
df = pd.read_csv("py/tngov -1.csv")

                            #Geojson data from url source 
with urlopen('http://www.openculture.gov.tn/dataset/70fd9b49-3925-477f-ae17-9d206d650aab/resource/4b3d85dd-a523-425c-b477-ab9fec6e51a0/download/decoupage.geojson') as response:
    cities = geojson.load(response)
print(cities['features'][0])

fig=px.choropleth_mapbox(df, geojson=cities,locations='id', color='population ', 
                                    color_continuous_scale="Viridis",hover_name = 'deleg_na_1', 
                                    hover_data =["gov_name_f","gov_id","population "],
                                    labels={'population':'population number'}, mapbox_style="carto-darkmatter",zoom=8,
                                    center = {"lat": 36.82189, "lon":10.168969 }, width=500,height=500,)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
#app layout 
app.layout = html.Div(children=[
            html.H1('JEUX DE DONNEES', style={'textAlign':'center', 'color':colors['H1']}),
            html.H2('Portail des données agricoles',style={'textAlign':'center', 'color':colors['text']}),
                    dcc.Graph(id='graph1',
                    figure={'data':[
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[108,104,116,127,112,113,131,109,94,96,82,112],
                        'type':'lines','name':'Bizerte'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[88,92,112,117,92,104,115,96,94,89,97,96],
                        'type':'lines','name':'Tunis carthage'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[86,88,107,112,88,98,111,100,90,94,82,94],
                        'type':'lines','name':'Kelibia'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[95,95,93,98,94,101,91,84,94,98,84,97],
                        'type':'lines','name':'Zaghouan-Mogran'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[96,101,106,127,106,105,119,115,99,105,91,104],
                        'type':'lines','name':'Beja'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[126,109,128,141,121,118,139,121,115,110,102,121],
                        'type':'lines','name':' Tabarka'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[94,84,111,99,86,93,104,98,93,78,81,104],
                        'type':'lines','name':' Le-kef'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[88,90,96,80,97,90,96,96,87,70,82,88],
                        'type':'lines','name':'tunisie centrale'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[68,61,62,44,76,65,61,71,56,62,61,68],
                        'type':'lines','name':'Kairouan'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[88,90,96,80,97,90,96,96,87,70,82,88],
                        'type':'lines','name':'tunisie centrale'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[68,61,62,44,76,65,61,71,56,62,61,68],
                        'type':'lines','name':'Kairouan'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[74,75,87,63,76,64,73,50,40,58,61,78],
                        'type':'lines','name':'Kasserine'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[86,85,86,87,113,63,32,95,93,77,83,111],
                        'type':'lines','name':'Thala'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[52,39,45,36,69,49,28,53,64,45,53,58],
                        'type':'lines','name':'Sidi-bouzid'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[56,46,59,35,53,53,44,61,60,52,53,61],
                        'type':'lines','name':'Mahdia'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[68,61,62,44,76,65,61,71,56,62,61,68],
                        'type':'lines','name':'Monastir'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[51,34,53,32,38,38,28,47,27,21,45,43],
                        'type':'lines','name':'Sfax'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[38,30,31,27,45,46,7,7,7,7,7,7],
                        'type':'lines','name':'Gabes'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[33,37,35,24,47,43,24,32,27,26,40,40],
                        'type':'lines','name':'Medenine'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[26,30,40,21,42,29,21,26,11,37,31,44],
                        'type':'lines','name':'Tataouine'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[40,33,38,29,37,48,32,34,34,45,42,44],
                        'type':'lines','name':'Jerba'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[37,29,36,31,47,32,22,33,35,24,36,40],
                        'type':'lines','name':'Gafsa'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[23,19,34,24,24,17,6,17,23,22,16,28],
                        'type':'lines','name':'Tozeur'
                        },
                        {'x':[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018],'y':[22,17,27,21,30,22,21,21,33,16,32,29],
                        'type':'lines','name':'Kebili'
                        },
                    ],
                        'layout':{
                            'title':'Bilan pluviometrique de la Tunisie de 2007- 2018', 'style':{'color': colors['text']}
                        }
                        }),
            dcc.Graph(id='graph2', 
                    figure={'data':[
                        {'x':[1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],
                        'y':[121,239,159,119,133,203,154,183,130,188,201,134,227,207,400,297,481,266,318,414],
                        'type':'lines','name':"nombre d'incendie"
                        },
                        {'x':[1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],
                        'y':[0,0,1375,2285,231,371,189,355,150,467,499,900,747,1700,2400,4200,6156,759,1680,17286],
                        'type':'lines','name':'surface'
                        },
                    ], 
                    'layout':{
                            'title':'Incendie de foret en Tunisie durant la periode 1998-2017',
                            'style':{'color': colors['text']}
                        }
                    }),
        dcc.Graph(id='graph3', 
                    figure={'data':[
                        {'x':[1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],
                        'y':[1549,1672400,1434200,1514800,1530400,1736100,1539700,1712500,1990900,2068500,1900700,2018100,2080000,2219000,2251000,2291800,2508200,2663200,2612000,2834000,2752998,3404800,3192904,3612295,2649000,0,0,0],
                        'type':'bar','name':"légumes_frais"
                        },
                        {'x':[1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],
                        'y':[75000,75000,86050,74050,69000,74000,85000,103000,103000,105000,105000,115000,111000,122000,113000,131000,124000,145000,162000,174000,190000,190000,195000,199000,223000,241000,260000],
                        'type':'bar','name':"dattes"
                        },
                        {'x':[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014],
                        'y':[1139000,566000,162400,370200,1424000,663000,1075500,915000,1016000,818000,770000,622000,986700,1125000,537000],
                        'type':'bar','name':"olives"
                        },
                        {'x':[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014],
                        'y':[140500,121000,113000,107000,127000,122000,132700,95000,122000,133000,129000,146671,151000,168000,174500],
                        'type':'bar','name':"raisins"
                        },
                        {'x':[1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014],
                        'y':[2195,1914,654,620,2867,1054,1665,1812,1086,1354,514,2904,2347,2097,1610,1988,1188,2533,1079,2310,2273,1295,2317],
                        'type':'bar','name':"céréale"
                        },
                        {'x':[1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],
                        'y':[761,840,760,314,374,534,353,520,584,422,302,321,627,608,650,551,904,798,897,964,933,966,904,695,544,778,824],
                        'type':'bar','name':"légumineuses"
                        },
                        {'x':[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],
                        'y':[225500,240000,240000,224100,209300,243100,262000,247100,299700,296900,307900,352000,360000,330000,355000,431000,378700,559600],
                        'type':'bar','name':"agrumes"
                        },
                        {'x':[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014],
                        'y':[310700,330000,310000,310000,375000,310000,365000,357000,370000,324000,370000,367000,340000,385000,463000],
                        'type':'bar','name':"plantes sarclées"
                        },
                        {'x':[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014],
                        'y': [2069000,1996000,2017500,2080000,2219000,2256000,2293000,2478000,2693000,2707000,2834000,2654000,2945000,3067000,3324000],
                        'type':'bar','name':"légumes frais jardins familiaux"
                        },
                        {'x':[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014],
                        'y': [3179000,4054000,3047600,4782000,4149000,3048000,3554000,4430800,4096400,4518000,3683100,4992400,4702900,4122600,5163800],
                        'type':'bar','name':"fourrages"
                        },
                    ],
                    'layout':{
                            'title':'Total de la production  récoltée  durant la periode 1991-2017',
                            'style':{'color': colors['text']}
                        }
                    }),
                dcc.Graph(id='choropleth', figure=fig),

            # dcc.Graph(id='choropleth',figure={'data':[
            #                 px.choropleth_mapbox(df, geojson=cities,locations='id', color='population ', 
            #                         color_continuous_scale="Viridis",hover_name = 'deleg_na_1', 
            #                         hover_data =["gov_name_f","gov_id","population "],
            #                         labels={'population':'population number'}, mapbox_style="carto-darkmatter",zoom=4,
            #                         center = {"lat": 36.82189, "lon":10.168969 }, width=500,height=500,)
            # ],
            # }),
])




if __name__ == '__main__':
    app.run_server()