from dash import html, dcc

from layout.data_table.layout import data_table_layout
from layout.header.layout import header_layout
from layout.details.layout import details_layout
from layout.button_array.layout import button_array_layout

from layout.table_buttons.layout import table_buttons_layout


def create_layout():
    layout = html.Div(
        [
            header_layout,

            details_layout,

            button_array_layout,

            table_buttons_layout,

            data_table_layout,
        ]
    )

    return layout
