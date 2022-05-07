from dash import html, dcc
import dash_bootstrap_components as dbc

lst = []
for item in range(30):
    lst.append(
        dbc.Button(
            f'but{str(item)}',
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

lst.append(dbc.Button(
    "Untagged",
    id="Untagged",
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
    }
))

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
    id="buttons_array",

)
