from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from dash.dependencies import State

import settings

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),
    html.Hr(),
    dcc.RadioItems(options=["pop", "lifeExp", "gdpPercap"], value="lifeExp", id="ctl-ratio-item"),
    html.Div([
        "Input: ",
        dcc.Input(id="my-input", value="initial value", type="text"),
    ]),
    html.Br(),
    html.Div(id='my-output'),
    dcc.Input(
        id='num-multi',
        type='number',
        value=5
    ),
    html.Table([
        html.Tr([html.Td(['x', html.Sup(2), "="]), html.Td(id='square')]),
        html.Tr([html.Td(['x', html.Sup(3), "="]), html.Td(id='cube')]),
        html.Tr([html.Td([2, html.Sup('x'), "="]), html.Td(id='twos')]),
        html.Tr([html.Td([3, html.Sup('x'), "="]), html.Td(id='threes')]),
        html.Tr([html.Td(['x', html.Sup('x'), "="]), html.Td(id='x^x')]),
    ]),
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'

@app.callback(
    Output('square', 'children'),
    Output('cube', 'children'),
    Output('twos', 'children'),
    Output('threes', 'children'),
    Output('x^x', 'children'),
    Input('num-multi', 'value'))
def callback_a(x):
    return x**2, x**3, 2**x, 3**x, x**x

@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'))
def update_output(n_clicks, input1, input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=settings.PORT)
