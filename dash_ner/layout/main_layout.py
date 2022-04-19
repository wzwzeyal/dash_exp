from dash import html

from layout.data_table.layout import data_table_layout
from layout.header.layout import header_layout
from layout.ner_buttons.layout import ner_buttons_layout
from layout.text.layout import text_layout


def create_layout():
    layout = html.Div(
        [
            header_layout,

            text_layout,

            ner_buttons_layout,

            data_table_layout,
        ]
    )

    return layout
