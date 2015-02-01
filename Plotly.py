# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
from Request import *

coords = data()

trace1 = Scatter(
    x=coords[0],
    y=coords[1],
    mode='markers',
    name='Device',
    text=['United States', 'Canada'],
    marker=Marker(
        color='rgb(164, 194, 244)',
        size=12,
        line=Line(
            color='white',
            width=0.5
        )
    )
)

data = Data([trace1])
layout = Layout(
    title='Network Users',
    xaxis=XAxis(
        title='X',
        showgrid=False,
        zeroline=False
    ),
    yaxis=YAxis(
        title='Y',
        showline=False
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='line-style')