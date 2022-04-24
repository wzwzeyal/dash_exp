import dash_bootstrap_components as dbc
from dash import html

from resources.strings import tag_button_names

lst = []
for count, item in enumerate(tag_button_names):
    lst.append(
        dbc.Button(
            item,
            id=item,
            outline=True,

            # id={
            #     'type': 'push-button',  # used for the group matching
            #     'index': count,  # index-key, item-value
            # },
            # className="m-1",
            style={
                "width": "120px",
                "color": 'black',
                'border': 'groove',
                # "padding": "5px",
                "margin-right": 5,
                "margin-bottom": 3,
                # "background-color": "white",
            }),
    )
    # "margin-bottom": "1%", "margin-right": "1%"}))

button_array_layout = html.Div(
    lst,
    style=
    {
        "margin": 10
    }
)
