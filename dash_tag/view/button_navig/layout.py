from dash import dcc, html

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
            style=dict(
                display="inline-block",
                fontSize=12,
                verticalAlign="top",
                borderStyle='groove',
                width=20,
            ),
        ),
    ],
    style={'margin': 10, }
)
