from dash import html, dcc

from view.NER.layout import ner_layout
from view.data_table.layout import data_table_layout
from view.header.layout import header_layout
from view.ner_button.layout import ner_button


def create_layout():
    layout = html.Div(
        [
            header_layout,

            ner_layout,

            ner_button,

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
