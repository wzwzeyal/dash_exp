from dash import html

text_layout = html.Div(
    [
        html.Div(
            id="text-button-container",
            children=[],
            style={
                'margin-left': 5,
                'textAlign': 'right',
                'direction': 'rtl',
            }),

        html.Br(),
    ]
)
