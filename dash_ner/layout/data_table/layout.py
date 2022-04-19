from dash import dash_table
from dash import html

from Data.data_frame import text_data_df

data_table_layout = html.Div(
    [
        dash_table.DataTable(
            text_data_df.to_dict('records'),
            columns=[dict(name='Text', id='comment')],
            id='text-data-table',

            style_table={
                'height': 400,
            },
            page_current=0,
            page_size=10,
            page_action='native',
            style_cell_conditional=[
                {
                    'if': {'column_id': 'comment'},
                    'direction': 'rtl'
                }
            ],
            style_data={
                'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            }
        ),

    ],
    style=dict(
        width='100%',
        # height='50%',
        # overflow='scroll',
        padding='10px 10px 10px 20px',
    )
)
