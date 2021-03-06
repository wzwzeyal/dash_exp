import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd

# from layout.data_table.layout import tag_data_df

data_df = pd.read_sql_table('test_tsv', "postgresql://postgres:postgres@localhost/test")

table_buttons_layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.RadioItems(
                                    id="page_size",
                                    className="btn-group",
                                    inputClassName="btn-check",
                                    labelClassName="btn btn-outline-primary",
                                    labelCheckedClassName="active",
                                    options=[
                                        {"label": "1", "value": "1"},
                                        {"label": "5", "value": "5"},
                                        {"label": "10", "value": "10"},
                                        {"label": "50", "value": "50"},
                                        {"label": "All", "value": "All"},
                                    ],
                                    value="10",
                                ),
                            ],
                            className="radio-group",
                            style={'margin-left': 10},
                        ),

                    ],
                    width="auto"
                ),

                dbc.Col(
                    html.Div(
                        dbc.Button(
                            [
                                "Untagged ",
                                dbc.Badge(len(data_df), id="badge", color="light", text_color="primary"),
                            ],
                            color="primary",
                            active=False,
                        ),
                    ),
                    width="auto",

                ),

                dbc.Col(

                    dbc.Progress(
                        id='tag-left-progress',
                        value=100,
                        style=
                        {
                            'height': 20,
                            'border': 'groove',
                            'width': '95%'
                        }
                    ),

                ),
            ],
            align='center',
        ),
    ],
)
