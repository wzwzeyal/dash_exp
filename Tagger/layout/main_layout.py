from dash import html, dcc

from layout.header.layout import header_layout
from layout.status.layout import status_layout
from layout.table.layout import table_layout
from layout.tag.layout import tag_layout


def create_layout():
    layout = html.Div(
        [
            header_layout,

            tag_layout,

            status_layout,

            table_layout,
        ],
        id='body',
    )

    return layout
