import dash_bootstrap_components as dbc
import pandas as pd
from dash import html

# from layout.data_table.layout import tag_data_df

data_df = pd.read_sql_table('test_tsv', "postgresql://postgres:postgres@localhost/test")

table_buttons_layout = html.Div(
    [
        html.Div(
            [
                html.Span(
                    'Tagged texts: '
                ),
                html.B(
                    "45",
                    id="nof-tagged-texts",
                    style={},
                ),
                html.Span(
                    " out of "
                ),
                html.Span(
                    "1000",
                    id="nof-total-texts"
                ),
            ],
        ),

        dbc.Progress(
            id='tag-left-progress',
            value=100,
            style=
            {
                'margin-left': '2em',
                # 'height': 20,
                # 'border': 'groove',
                'width': '60%',
                'height': '5px'
            },
        ),
    ],
    style={
        'display': 'flex',
        # 'margin': '1em',
        # 'flex-wrap': 'nowrap',
        'grid-column': '1 / -1',
        'align-items': 'center',
        # 'display': 'inline',
    },
)
