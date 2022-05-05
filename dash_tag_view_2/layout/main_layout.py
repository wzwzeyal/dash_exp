import dash_bootstrap_components as dbc
from dash import html

from layout.button_array.layout import button_array_layout
from layout.data_table.layout import data_table_layout
from layout.details.layout import details_layout
from layout.header.layout import header_layout
from layout.table_buttons.layout import table_buttons_layout


def create_layout():
    layout = html.Div(

        [
            header_layout,

            details_layout,

            button_array_layout,

            table_buttons_layout,

            data_table_layout,
        ],
        style={
            'display': 'grid',
            'grid-template-columns': '3fr 1fr',
            'grid-template-rows': '7% auto 5% auto',
            'position': 'absolute',
            'padding': '10px',
            'top': 0,
            'bottom': 0,
            'height': '100%',
            'width': '100%',
        }
    )
    return layout
