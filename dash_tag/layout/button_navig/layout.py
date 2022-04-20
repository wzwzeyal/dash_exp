import dash_bootstrap_components as dbc
from dash import dcc, html

button_navig_layout = html.Div(
    [
        html.Span(
            "My very own text to copy ",
            id="textarea_id",
            style={'margin-right': -2, 'borderStyle': 'groove'}),

        dcc.Clipboard(
            target_id="textarea_id",
            title="copy",
            style={
                'display': "inline-block",
                'fontSize': 12,
                'verticalAlign': "top",
                'borderStyle': 'groove',
                'width': 20,
                'margin-right': 10
            },
        ),
    ],
    style={'margin': 10, }
)
