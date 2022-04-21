import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, Input, Output, no_update
from dash import dash_table
from dash import html

app = Dash(
    __name__, )

df = pd.read_csv('../dash_tag/resources/test.tsv', sep='\t')
df['id'] = df.index

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

        dbc.Button(
            "Button",
            id="change-table",
        ),
        dash_table.DataTable(
            id='records-data-table',
            data=df.to_dict('records'),
            columns=[
                dict(name='Tag', id='tag', presentation='dropdown'),
                dict(name='Text', id='comment')],
            # columns=[{'id': c, 'name': c} for c in df.columns],
            page_current=0,
            page_size=100,
            page_action='native',
            style_table={'height': '300px', 'overflowY': 'auto'},
            style_data={
                'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                'overflow': 'hidden',
            },
            editable=True,
            dropdown=
            {
                'tag': {
                    'options': [
                        {'label': i, 'value': i}
                        for i in [
                            'Untagged',
                            'Tag1',
                            'Tag2',
                        ]
                    ]
                },
            },

        ),

        dbc.Row(
            [
                dbc.Col(html.Div(
                    "One of three columns",
                    id="one",
                )),
                dbc.Col(html.Div(
                    "Two of three columns"),
                    id="two",
                ),
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


@app.callback(
    Output('records-data-table', 'data'),
    Input('change-table', 'n_clicks'),  # -2
)
def on_change_table(n_clicks):
    df.at[0, "comment"] = str(n_clicks)
    return df.to_dict('records')


@app.callback(
    Output('one', 'children'),
    Output('two', 'children'),
    Input('records-data-table', 'active_cell'),
    Input('records-data-table', 'derived_viewport_data')
)
def on_active_cell(active_cell, viewport_data):
    if viewport_data is None:
        return no_update

    if active_cell is None:
        return no_update

    print(viewport_data[active_cell['row']])
    return str(viewport_data[active_cell['row']]['comment']), str(len(viewport_data))


if __name__ == '__main__':
    app.run_server(debug=True)
