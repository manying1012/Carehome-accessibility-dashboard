from urllib.request import urlopen
from dash import Dash, html, dcc

app = Dash(__name__)

import json
with urlopen('https://raw.githubusercontent.com/gausie/LSOA-2011-GeoJSON/master/lsoa.geojson') as response:
    lsoa = json.load(response)
    
import pandas as pd
df = pd.read_csv("DRAFT Care Access Index England.csv", dtype={"lsoa11cd": str})

import plotly.express as px
fig = px.choropleth(df, geojson=lsoa, locations='lsoa11cd', featureidkey="properties.LSOA11CD", color='pop_adjusted_beds',
                           color_continuous_scale="Viridis",
                           labels={'pop_adjusted_beds':'population adjusted beds'}
                          )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app.layout = html.Div(children=[
    html.H1(children='Carehome accessibility'),

    html.Div(children='''
        Carehome accessibility across the UK.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
