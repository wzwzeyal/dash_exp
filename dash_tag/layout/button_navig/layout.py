from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_react_wordcloud

from dash_react_wordcloud import DashReactWordcloud

button_navig_layout = html.Div(
    # button_navig_layout = dbc.Container(
    [
        html.Span("Label 1", style={'margin-right': 10, 'borderStyle': 'groove'}),

        html.Span("Label 2", style={'margin-right': 10, 'borderStyle': 'groove'}),

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

        dbc.Button(
            "show-all",
            id='show-all',
            style={
                'margin-right': 10
            },
        ),

        dbc.Button(
            "show-untagged",
            id='show-untagged',
        ),
    ],
    style={'margin': 10, }
)
