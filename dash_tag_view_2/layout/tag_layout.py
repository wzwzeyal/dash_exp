import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html, dcc

lst = []
for item in range(30):
    lst.append(
        dbc.Button(
            item,
            id=f'but{str(item)}',
            outline=True,
            style={
                # "width": "120px",
                "color": 'black',
                'border': 'groove',
                # "padding": "5px",
                "margin-right": 5,
                "margin-bottom": 3,
                "display": "inline",
                # "background-color": "white",
            }),
    )

lst.append(dbc.Button(id="Untagged"))

buttons_array = html.Div(
    [
        html.Div(
            lst[:20],
            style={'border-style': 'none', 'height': '65%', 'margin-top': '10px'}

        ),
        html.Div(
            lst[20:],
            style={'border-style': 'none', 'height': '35%', 'margin-top': '10px'}
        ),
    ],
    style={'display': 'flex', 'flex-direction': 'column', 'height': '100%'}
)

row_details = html.Div(
    [
        dbc.Textarea(id="left-textarea-example", placeholder="1", style={'border-style': 'none', 'height': '45%'}),
        dbc.Textarea(id="right-textarea-example", placeholder="2", style={'border-style': 'none', 'height': '45%'}),

        html.Div(
            [
                # html.Div(
                #     dbc.Textarea(placeholder="3.1", style={'width': '99%', 'height': '87%'}),
                #     style={'flex': '1', 'background-color': 'green'}
                # ),
                # dbc.Textarea(placeholder="3.2", style={'flex': '1'}),
                # dbc.Textarea(placeholder="3.3", id="textarea_id", style={'flex': '1'})
                html.Span(
                    [
                        "textarea_id",
                        dcc.Clipboard(
                            target_id="textarea_id",
                            style={
                                "position": "absolute",
                                "top": 2,
                                "right": 2,
                                "fontSize": 20,
                            },
                        ),
                    ],
                    id="textarea_id",
                    style={'flex': '1', "position": "relative", 'border': '1px solid'}),
                html.Span("Text2", style={'flex': '1', 'border': '1px solid'}, ),
                html.Span("Text3", style={'flex': '1', 'border': '1px solid'}),

            ],
            # style={'display': 'grid', 'grid-auto-flow': 'column', 'grid-auto-columns': '1fr'},
            style={'display': 'flex', 'gap': '10px', 'height': '7%', 'align-content': 'start'}
        ),
    ],
    style={'display': 'flex', 'flex-direction': 'column', 'height': '100%', 'width': '96%',
           'margin-left': '2%'}
)

tag_layout = html.Div(
    [
        html.Div([row_details], style={'width': '70%', }),
        html.Div(
            style={
                'border': '2px solid #eff2f5',
                'margin-top': '2%',
                'height': '89%',
                'margin-right': '10px'
            }),
        html.Div([buttons_array], style={'width': '30%', }),
    ],
    style={
        'display': 'flex',
        'background-color': '#ffffff',
        'height': '100%',
    }
)
