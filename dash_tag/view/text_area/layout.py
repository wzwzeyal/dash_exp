from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

text_area_layout = html.Div(
    [
        dcc.Textarea(
            id='left-textarea-example',
            value='left-textarea-example',
            readOnly=True,
            style={'width': '45%', 'height': 100, 'margin-right': 5},

        ),

        dcc.Textarea(
            id='right-textarea-example',
            value='right-textarea-example',
            readOnly=True,
            style={'width': '45%', 'height': 100},  # 'margin': '2%'},  # 'margin-left': "10%"},

        ),

    ],
    style={'margin': 10}
)
