import dash_bootstrap_components as dbc
from dash import html

from resources.strings import tag_button_names



lst = []
for count, item in enumerate(tag_button_names):
    lst.append(
        dbc.Button(
            item,
            id=item,
            # id={
            #     'type': 'push-button',  # used for the group matching
            #     'index': count,  # index-key, item-value
            # },
            className="m-1",
            style={
                # "width": "70px",

                # "padding": "5px",
                # "margin": "0.1%",
                # "background-color": "white",
            }),
    )
    # "margin-bottom": "1%", "margin-right": "1%"}))

button_array_layout = html.Div(
    lst
)

# button_array_layout = dbc.ButtonGroup(
#     lst
# )

# btn_options = [
#     {"label": "Option 1", "value": 1},
#     {"label": "Option 2", "value": 2},
#     {"label": "Option 3", "value": 3},
#     {"label": "Option 4", "value": 4},
#     {"label": "Option 1", "value": 1},
#     {"label": "Option 2", "value": 2},
#     {"label": "Option 3", "value": 3},
#     {"label": "Option 4", "value": 4},
#     {"label": "Option 1", "value": 1},
#     {"label": "Option 2", "value": 2},
#     {"label": "Option 3", "value": 3},
#     {"label": "Option 4", "value": 4},
#     {"label": "Option 1", "value": 1},
#     {"label": "Option 2", "value": 2},
#     {"label": "Option 3", "value": 3},
#     {"label": "Option 4", "value": 4},
# ]


# button_array_layout = html.Div(
#     [
#         dbc.RadioItems(
#             id="radios",
#             className="btn-group",
#             inputClassName="btn-check",
#             labelClassName="btn btn-outline-primary",
#             labelCheckedClassName="active",
#             options=btn_options,
#             # [
#             #       {"label": "Option 1", "value": 1},
#             #       {"label": "Option 2", "value": 2},
#             #       {"label": "Option 3", "value": 3},
#             #   ],
#             value=1,
#             style={"padding": "0px", "margin": "0px"}
#         ),
#         html.Div(id="output"),
#     ],
#     className="radio-group",
#     style={"margin-left": 10}
# )

# @app.callback(Output('container', 'children'),
#               # input_callback,
#               )
# def display(*arg):
#     ctx = callback_context
#     button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#     print(button_id)
#     # print(len(arg))
#     # print(ctx)
#     return no_update
