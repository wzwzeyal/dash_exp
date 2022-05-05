import dash_bootstrap_components as dbc
from dash import dcc, html

from layout.button_array.layout import button_array_layout

details_layout = html.Div(
    [
        dbc.Textarea(
            id='left-textarea-example',
            value='left-textarea-example',
            readOnly=True,
            style={
                # 'width': '49%',
                'height': '45%',
                'direction': 'rtl',
                'border-style': 'none',
            },

        ),

        dbc.Textarea(
            id='right-textarea-example',
            value='right-textarea-example',
            readOnly=True,
            style={
                # 'width': '49%',
                'height': '45%',
                'direction': 'rtl',
                'border-style': 'none',
            },
        ),

        html.Div(
            [
                # TODO: Add clipboard
                dbc.Textarea(placeholder="3.1",),
                dbc.Textarea(placeholder="3.2",),
                dbc.Textarea(placeholder="3.3",),
            ],
            style=
            {
                'display': 'grid',
                'grid-template-columns': '1fr 1fr 1fr',
                'height': '10%',
            },
        ),
    ],
    id="details",
    style={
        # 'grid-column-start': '1',
        # 'grid-column-end': '2',
        #
        # "borderStyle": "groove",
        # "display": "inline",
    }
)