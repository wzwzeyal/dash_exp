from dash import dash_table
from dash import html

from dash_tag.data.data_frame import tag_model_df

data_table_layout = html.Div(
    [
        dash_table.DataTable(
            tag_model_df.to_dict('records'),
            # [{"name": i, "id": i} for i in tag_model_df.columns],
            id='records-data-table',
            columns=[
                dict(name='Tag', id='tag'),
                dict(name='Copy', id='copy_text'),
                dict(name="random2", id="random2"),
                dict(name="random1", id="random1"),
                dict(name='Right Text', id='reverse'),
                dict(name='Left Text', id='comment'),
            ],
            page_current=0,
            page_size=100,
            page_action='native',
            style_table={
                'height': '400px',
                'overflowY': 'auto'
            },
            filter_action='native',
            style_data={
                'maxWidth': '150px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            }
        ),

    ],
    style=
    {
        'width': '98%',
        'margin': '10',
        # 'overflow-y': 'scroll',
    },
    # style=dict(
    #     width='98%',
    #     margin=10,
    #     # overflow-y: scroll
    #     # height='50%',
    #     # overflow='scrollY',
    #     # padding='10px 10px 10px 20px',
    # ),
)

# data_table_layout = dash_table.DataTable(
#     # columns=[
#     #     {'name': 'Continent', 'id': 'continent', 'type': 'numeric'},
#     #     {'name': 'Country', 'id': 'country', 'type': 'text'},
#     #     {'name': 'Population', 'id': 'pop', 'type': 'numeric'},
#     #     {'name': 'Life Expectancy', 'id': 'lifeExp', 'type': 'numeric'},
#     #     {'name': 'Mock Dates', 'id': 'Mock Date', 'type': 'datetime'}
#     # ],
#     data=model_df.to_dict('records'),
#     filter_action='native',
#
#     style_table={
#         'height': 400,
#     },
#     style_data={
#         'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
#         'overflow': 'hidden',
#         'textOverflow': 'ellipsis',
#     }
# )
