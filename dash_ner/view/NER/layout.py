from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

# from Model.data_frame import text
#
# ner_text_btn_lst = []
#
# split_text = text.split(' ')
#
# for count, value in enumerate(split_text):
#     ner_text_btn_lst.append(
#         dbc.Button(
#             value,
#             id=str(count),
#             className="me-1",
#             outline=True,
#             style={
#                 "color": "black",
#                 # "border": "2px solid #4CAF50",
#                 # "background-color": "white",
#                 "padding": 0,
#             },
#         )
#     )

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

ner_layout = html.Div(
    [
        html.Div(
            id="text-button-container",
            children=[],
            style={
                'margin-left': 5,
                'textAlign': 'right',
                'direction': 'rtl',
            }),

        # dcc.store("style_array", ),
    ]
)
