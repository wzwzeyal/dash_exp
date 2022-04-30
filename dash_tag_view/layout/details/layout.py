import dash_bootstrap_components as dbc
from dash import dcc, html

details_layout = html.Div(
    [
        dbc.Textarea(
            id='left-textarea-example',
            value='left-textarea-example',
            readOnly=True,
            style={
                'width': '49%',
                'height': 400,
                'direction': 'rtl',
                'border-style': 'none',
                # 'margin-right': '2%',
                'display': 'inline'
            },

        ),

        # html.Spacer(
        #     style={
        #         'width': '10%',
        #         'display': 'inline',
        #     }
        # ),

        dbc.Textarea(
            id='right-textarea-example',
            value='right-textarea-example',
            readOnly=True,
            style={
                'width': '49%',
                'height': 400,
                'direction': 'rtl',
                'border-style': 'none',
                'display': 'inline',
                'position': 'absolute',
                'right': 10,
            },
            # 'margin': '2%'},  # 'margin-left': "10%"},

        ),

        html.Div(
            [
                dbc.Textarea(
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
            ], style={"width": "100%"}
        ),
    ],
    id="details",
    style={'margin': 10, "borderStyle": "none"}
)