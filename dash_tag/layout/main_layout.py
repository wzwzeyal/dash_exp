from dash import html, dcc

from layout.data_table.layout import data_table_layout
from layout.header.layout import header_layout
from layout.text_area.layout import text_area_layout
from layout.button_array.layout import button_array_layout
from layout.button_navig.layout import button_navig_layout


def create_layout():
    layout = html.Div(
        [
            header_layout,

            text_area_layout,

            button_navig_layout,

            button_array_layout,

            html.Br(),

            data_table_layout,
        ]
    )

    return layout
    # app.layout = html.Div([
    #     html.Div(children=[
    #         html.Label('Dropdown'),
    #         dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
    #
    #         html.Br(),
    #         html.Label('Multi-Select Dropdown'),
    #         dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'],
    #                      ['Montréal', 'San Francisco'],
    #                      multi=True),
    #
    #         html.Br(),
    #         html.Label('Radio Items'),
    #         dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
    #     ], style={'padding': 10, 'flex': 1}),
    #
    #     html.Div(children=[
    #         html.Label('Checkboxes'),
    #         dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
    #                       ['Montréal', 'San Francisco']
    #                       ),
    #
    #         html.Br(),
    #         html.Label('Text Input'),
    #         dcc.Input(value='MTL', type='text'),
    #
    #         html.Br(),
    #         html.Label('Slider'),
    #         dcc.Slider(
    #             min=0,
    #             max=9,
    #             marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
    #             value=5,
    #         ),
    #     ], style={'padding': 10, 'flex': 1})
    # ], style={'display': 'flex', 'flex-direction': 'row'})
