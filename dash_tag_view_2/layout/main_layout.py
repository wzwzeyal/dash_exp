from dash import html, dcc

from layout.status_layout import status_layout
from layout.table_layout import table_layout
from layout.tag_layout import tag_layout
from layout.header import header_layout


def create_layout():
    layout = html.Div(
        [
            html.Div([header_layout], style={'height': '5%', 'width': '95%', 'margin-left': '2%'}),

            html.Div([tag_layout], style={'height': '70%', 'width': '95%', 'margin-left': '2%'}),

            html.Div([status_layout], style={'height': '10%', 'width': '95%', 'margin-left': '2%'}),

            html.Div([table_layout], style={'height': '70%', 'width': '95%', 'margin-left': '2%'}),

            # table_layout,
        ],
        id='body',
        style={
            'background-color': '#eff2f5',
            'position': 'absolute',
            'top': 0,
            'bottom': 0,
            'height': '100%',
            'width': '100%',
        }
    )

    return layout
