from dash import html
import dash_bootstrap_components as dbc

from Data.data_frame import ner_value

ner_btn_lst = []

for index, value in enumerate(ner_value):
    ner_btn_lst.append(
        dbc.Button(
            value,
            id=value,
            className="me-3",
            style={
                "color": value,
            }
        ),
    )

ner_buttons_layout = html.Div(
    ner_btn_lst,
    style={
        'margin-left': 5,
        'textAlign': 'right',
        'direction': 'rtl',
    },
)
