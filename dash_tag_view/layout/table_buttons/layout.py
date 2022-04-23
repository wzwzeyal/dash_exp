import dash_bootstrap_components as dbc
from dash import html, dcc

from data.data_frame import tag_model_df

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
                        [
                            dbc.RadioItems(
                                id="filter-table",
                                className="btn-group",
                                inputClassName="btn-check",
                                labelClassName="btn btn-outline-primary",
                                labelCheckedClassName="active",
                                options=[
                                    {"label": "Show Untagged", "value": 1},
                                    {"label": "Show All", "value": 2},
                                ],
                                value=1,
                            ),
                        ],
                        className="radio-group",
                    ),
                    width="auto",
                ),

                dbc.Col(
                    html.Div(
                        dbc.Button(
                            [
                                "Untagged ",
                                dbc.Badge(len(tag_model_df), id="badge", color="light", text_color="primary"),
                            ],
                            color="primary",
                            active=False,
                        ),
                    ),
                    width="auto",

                ),
                dbc.Col(
                    dcc.Input(
                        id='text-filter',
                        type='text',
                        debounce=False,
                        placeholder="Search for text",

                    ),
                    width="auto",
                ),
                dbc.Col(

                    dbc.Progress(
                        id='tag-complete-progress',
                        value=0,

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
        html.Br(),
    ],
)
