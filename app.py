import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart
cereals=['Apple Jacks', 'Cinnamon Toast Crunch', 'Fruit Loops', 'Frosted Flakes','Lucky Charms','Quaker Oat Squares','Special K']
protein=[2, 1, 2, 1, 2, 4, 6]
sugars=[14, 9, 13, 11, 12, 6, 3]
cups=[1, 0.75, 1, 0.75, 1, 0.5, 1]
color1='orange'
color2='darkred'
color3='purple'

protein = go.Bar(
    x=cereals,
    y=protein,
    name='Protein',
    marker={'color':color1}
)
sugars = go.Bar(
    x=cereals,
    y=sugars,
    name='Sugar',
    marker={'color':color2}
)
cups = go.Bar(
    x=cereals,
    y=cups,
    name='Serving Size',
    marker={'color':color3}
)
beer_data = [protein, sugars, cups]
beer_layout = go.Layout(
    barmode='group',
    title = 'Cereal Nutrition'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Flying Dog Beers'),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href='https://github.com/austinlasseter/flying-dog-beers'),
    html.Br(),
    html.A('Data Source', href='https://www.flyingdog.com/beers/'),
    ]
)

if __name__ == '__main__':
    app.run_server()
