from dash import dcc, html

details_layout = html.Div(
    [
        dcc.Textarea(
            id='left-textarea-example',
            value='left-textarea-example',
            readOnly=True,
            style={'width': '48%', 'height': 400, 'direction': 'rtl', 'border-style': 'none', 'margin-right': '2%'},

        ),

        dcc.Textarea(
            id='right-textarea-example',

            value='right-textarea-example',
            readOnly=True,
            style={'width': '50%', 'height': 400, 'direction': 'rtl', 'border-style': 'none'},  # 'margin': '2%'},  # 'margin-left': "10%"},

        ),

        html.Br(),

        html.Div(
            [
                dcc.Textarea(
                    id="textarea_id",
                    style={'width': '100%', "overflow": "auto", "borderStyle": "groove"},
                ),
                dcc.Clipboard(
                    target_id="textarea_id",
                    style={
                        "position": "absolute",
                        "top": 0,
                        "right": 20,
                        "fontSize": 20,
                    },
                ),
            ], style={"width": "100%", "position": "relative"}
        ),
    ],
    style={'margin': 10}
)
