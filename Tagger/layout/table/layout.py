import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html, dcc, dash_table

data_df = pd.read_sql_table('test_tsv', "postgresql://postgres:postgres@localhost/test")
data_df.sort_values(by='tag_id', inplace=True)
data_df.set_index('tag_id', inplace=True, drop=False)

tagged_df = data_df[~data_df['tag'].str.contains('Untagged')]

table_layout = html.Div(
    [

        dash_table.DataTable(
            tagged_df.head(10).to_dict('records'),
            # [{"name": i, "id": i} for i in tag_data_df.columns],
            id='records-data-table',
            columns=
            [
                dict(name='Tag', id='tag'),
                dict(name='Copy', id='copy_text', ),
                dict(name="random2", id="random2", ),
                dict(name="random1", id="random1", ),
                dict(name='Right Text', id='reverse', ),
                dict(name='Left Text', id='comment'),
                # dict(name='Tag Id', id='tag_id'),
            ],
            page_current=0,
            page_size=10,
            page_action='native',
            style_table={
                'max-height': '400px',
                'overflowY': 'auto'
            },
            sort_action='native',
            filter_action='native',
            editable=True,
            style_data=
            {
                'maxWidth': '150px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            style_data_conditional=[
                {
                    'if': {
                        'state': 'active'  # 'active' | 'selected'
                    },
                    'backgroundColor': 'white'
                },
                {
                    'if': {
                        'state': 'selected'  # 'active' | 'selected'
                    },
                    'backgroundColor': 'white'
                },
            ],
        ),

    ],

    className="base_layout",
    style=
    {
        'position': 'absolute',
        'left': 10,
    },
)
