from dash import html

header_layout = html.Div(
    [
        html.H1("Dash Tag"),
        html.Div(id='container'),
    ], style={'textAlign': 'center'},
)
