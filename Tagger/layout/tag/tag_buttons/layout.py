from dash import html, dcc
import dash_bootstrap_components as dbc

from resources.strings import tag_button_names

lst = []
for item in range(30):
    lst.append(
        dbc.Button(
            f'{tag_button_names[item]}',
            id=f'but{str(item)}',
            outline=True,
            # className="tag_button",
            style={
                # "width": "120px",
                "color": 'black',
                'border': 'groove',
                # "padding": "5px",
                "margin-right": 5,
                "margin-bottom": 3,
                "display": "inline",
                # "background-color": "white",
            },
        ),
    )

buttons_array = html.Div(
    [
        html.Div(
            lst[:20],
            className="button_array",
            # style={'height': '65%', }

        ),
        html.Div(
            lst[20:],
            className="button_array",
            # style={'height': '35%', }
        ),
    ],
    id="buttons_array",

)
