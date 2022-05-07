from dash import html, dcc

from layout.tag.buttons_array_layout import buttons_array
from layout.tag.row_details_layout import row_details

tag_layout = html.Div(
    [
        row_details,
        html.Div(className="tag_spacer"),
        buttons_array,
    ],
    id="tag_layout",
    className="base_layout",
)
