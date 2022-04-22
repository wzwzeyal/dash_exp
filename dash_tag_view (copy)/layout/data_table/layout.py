from dash import dash_table, dcc
from dash import html


data_table_layout = html.Div(
    [
        dcc.Interval(id='interval_pg', interval=86400000 * 7, n_intervals=0),
        # activated once/week or when page refreshed
        html.Div(id='postgres_datatable', children=[]),


    ],
    style=
    {
        'width': '98%',
        # 'display': 'flex',
        # 'margin-left': '20',
        # 'overflow-y': 'scroll',
    },
)
