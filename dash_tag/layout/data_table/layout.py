import dash_bootstrap_components as dbc
from dash import dash_table
from dash import html

from data.data_frame import tag_model_df

data_table_layout = html.Div(
    [
        # html.Div(
        #     id='table-status-div',
        #     children=dbc.Alert(
        #         f'Only {len(tag_model_df)} left, keep up the good work !',
        #         id='table-status',
        #         color='primary',
        #         # children=html.Div(str(len(tag_model_df))),
        #         # disabled=True,
        #     ),
        # ),
        dbc.Row(
            [
        dbc.Alert(
            f'Only {len(tag_model_df)} left, keep up the good work !',
            id='table-status',
            color='primary',
            style=
            {
                'height': '20px',
                'width': '30%'
            }
            # children=html.Div(str(len(tag_model_df))),
            # disabled=True,
        ),

        dbc.Progress(
            id='tag-complete-progress',
            value=0,
            style=
            {
                'width': '30%'
            }
        ),
                ]),

        dbc.Button(
            [
                "Notifications",
                dbc.Badge("4", id="badge", color="light", text_color="primary", className="ms-1"),
            ],
            color="primary",
        ),

        html.Br(),

        # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button_group/
        html.Div(
            [
                dbc.RadioItems(
                    id="radios",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-primary",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "Show All", "value": 1},
                        {"label": "Show Untagged", "value": 2},
                    ],
                    value=1,
                ),
                html.Div(id="output"),
            ],
            className="radio-group",
        ),

        html.Div(
            [
                dbc.RadioItems(
                    id="page_size",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-primary",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "5", "value": 5},
                        {"label": "10", "value": 10},
                        {"label": "20", "value": 20},
                    ],
                    value=5,
                ),
                # html.Div(id="output"),
            ],
            className="radio-group",
        ),

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
            page_size=5,
            page_action='native',
            style_table={
                'height': "50%",
                'overflow': 'scroll',
            },
            filter_action='native',
            style_data={
                'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            }
        ),

    ],
    style=dict(
        width='100%',
        height='50%',
        overflow='scrollY',
        padding='10px 10px 10px 20px',
    )
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
