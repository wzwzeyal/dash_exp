from dash import html
import dash_bootstrap_components as dbc

header_layout = html.Div(
    [
        html.H1("Dash NER"),
        html.Div(id='container'),
        # dbc.Store(id='selected_indices')
    ], style={'textAlign': 'center'},
)
