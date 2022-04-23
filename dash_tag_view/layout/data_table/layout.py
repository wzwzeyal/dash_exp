from dash import dash_table, dcc
from dash import html

from data.data_frame import tag_model_df

data_table_layout = html.Div(
    [
        dash_table.DataTable(
            tag_model_df.head(10).to_dict('records'),
            # [{"name": i, "id": i} for i in tag_model_df.columns],
            id='records-data-table',
            columns=[
                dict(name='Tag', id='tag', ),
                dict(name='Copy', id='copy_text', ),
                dict(name="random2", id="random2", ),
                dict(name="random1", id="random1", ),
                dict(name='Right Text', id='reverse', ),
                dict(name='Left Text', id='comment', ),
            ],
            page_current=0,
            page_size=1,
            page_action='custom',
            style_table={
                'max-height': '400px',
                'overflowY': 'auto'
            },
            # sort_action='native',
            # filter_action='native',
            editable=True,
            style_data=
            {
                'maxWidth': '150px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },

        ),

    ],
    style=
    {
        'width': '98%',
        # 'display': 'flex',
        # 'margin-left': '20',
        # 'overflow-y': 'scroll',
    },
)
