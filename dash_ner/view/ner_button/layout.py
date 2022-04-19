from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

from Data.data_frame import ner_value

ner_btn_lst = []

for index, value in enumerate(ner_value):
    ner_btn_lst.append(
        dbc.Button(
            value,
            id=value,
            className="me-3",
            # # outline=True,
            style={
                "color": value,
                # "border": "2px solid #4CAF50",
                # "background-color": "white",
                # "padding": 0,
            }

        ),
    )

# button_lst = [
#     dbc.Button(
#         "first_unclassified_word",
#         className="me-1",
#         outline=True,
#         style={
#             "color": "black",
#             # "border": "2px solid #4CAF50",
#             "background-color": "white",
#             "padding": 0,
#         }
#
#     ),
#
#     dbc.Button(
#         "some_second_classified_word",
#         className="me-1",
#         outline=True,
#         style={
#             "color": "black",
#             "border": "2px solid #4CAF50",
#             "background-color": "white",
#             "padding": 0
#         }
#
#     ),
# ]

ner_button = html.Div(
    ner_btn_lst,
    style={
        'margin-left': 5,
        'textAlign': 'right',
        'direction': 'rtl',
    },
)
