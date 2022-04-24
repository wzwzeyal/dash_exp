from dash import html, dcc

from dash_tag.layout.data_table.layout import data_table_layout
from dash_tag.layout.header.layout import header_layout
from dash_tag.layout.details.layout import details_layout
from dash_tag.layout.button_array.layout import button_array_layout

from dash_tag.layout.table_buttons.layout import table_buttons_layout


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
