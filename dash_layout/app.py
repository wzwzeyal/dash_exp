import dash_bootstrap_components as dbc
from dash import Dash
from dash import html

app = Dash(
    __name__, )

# app.layout = html.Div(
#     [
#         dbc.Button("Button1", style={'width': '10%'}, outline=True, color="warning"),
#
#         dbc.Button("Button2", style={'width': '10%'}),
#
#         dbc.Textarea("Text", style={'width': '30%'}),
#
#     ], style={'display': 'flex', 'gap': '5px', 'margin': '10px', }  # className="flex-container",
# )

app.layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div(
                    [
                        dbc.Progress(
                            id='tag-complete-progress',
                            value=10,
                        ),
                    ])),
            ]
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
