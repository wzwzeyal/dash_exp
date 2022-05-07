from dash import html

from layout.tag.tag_buttons.layout import buttons_array
from layout.tag.tag_data.layout import row_details

tag_layout = html.Div(
    [
        row_details,
        html.Div(className="tag_spacer"),
        buttons_array,
    ],
    id="tag_layout",
    className="base_layout",
)
