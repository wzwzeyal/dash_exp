import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html, dcc

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df[' index'] = range(1, len(df) + 1)
app = Dash(__name__)
PAGE_SIZE = 5

row_details = html.Div(
    [

        dbc.Textarea(placeholder="1", style={'border-style': 'none', 'height': '50%'}),
        dbc.Textarea(placeholder="2", style={'border-style': 'none', 'height': '50%'}),

        html.Div(
            [
                # html.Div(
                # dbc.Textarea(
                #             id="textarea_id",
                #             value="Copy and paste helkhjklh lkjh ",
                #         ),
                # ),


                # html.Div(
                #     [
                #
                #         # dcc.Clipboard(
                #         #     target_id="textarea_id",
                #         #     title="copy",
                #         #     style={
                #         #         "position": "absolute",
                #         #         "top": 0,
                #         #         "right": 0,
                #         #         "fontSize": 20,
                #         #     },
                #         # ),
                #     ],
                #     style={'width': '100%'}
                # ),
                html.Div(
                dbc.Textarea(placeholder="4", style={'border-style': 'none', 'width': '100%'}),
                ),
                # html.Div(
                # dbc.Textarea(placeholder="5",),
                # ),
            ],
            style={'display': 'grid', 'grid-auto-flow': 'column', 'grid-auto-columns': '1fr'},
            # style={'display': 'flex', 'width': '100%'}
        ),
    ],
    style={'display': 'flex', 'flex-direction': 'column', 'height': '100%'}
)

buttons_array = html.Div(
    [
        dbc.Textarea(placeholder="1", style={'border-style': 'none', 'height': '50%'}),
        dbc.Textarea(placeholder="2", style={'border-style': 'none', 'height': '50%'}),
    ],
    style={'display': 'flex', 'flex-direction': 'column', 'height': '100%'}
)

main_layout = html.Div(
    [
        html.Div([row_details], style={'width': '75%', }),
        html.Div(
            style={
                'border': '2px solid #eff2f5',
                'margin-top': '2%',
                'height': '90%',
                'margin-right': '10px'
            }),
        html.Div([buttons_array], style={'width': '25%', }),
    ],
    style={
        'display': 'flex',
        'background-color': '#ffffff',
        'height': '100%',
    }
)

app.layout = html.Div(
    [
        html.Div("header", style={'height': '5%', }),
        html.Div([main_layout], style={'height': '60%', }),
        html.Div("status", style={'height': '5%', }),
        html.Div("table", style={'height': '30%', }),
    ],
    id='body',
    style={
        'display': 'flex',
        'flex-direction': 'column',
        'background-color': '#eff2f5',
        # 'flex-grow': '1',

        'position': 'absolute',
        'top': 0,
        'bottom': 0,
        'height': '100%',
        'width': '100%',
    }
)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
