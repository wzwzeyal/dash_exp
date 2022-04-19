import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
from dash import Dash, dash_table

from Model.data_frame import no_but_model_df

# data_table_layout = html.Div(
#     dbc.Table.from_dataframe(model_df, striped=True, bordered=True, hover=True)
# )



data_table_layout = html.Div(
    [
        dbc.Input(
            id='selected-row-id',
            type="number",
            # disabled=True,
        ),

        dbc.Progress(
            id='but-complete',
            value=50),

        dash_table.DataTable(
            no_but_model_df.to_dict('records'),
            [{"name": i, "id": i} for i in no_but_model_df.columns],
            id='model',
            filter_action='native',
            row_selectable="single",
            # selected_rows=
            style_table={
                'height': 400,
            },
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
        overflow='scroll',
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