# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# sudo kill $(sudo lsof -t -i:8050)
from dash import Dash, Input, Output, State, no_update, callback_context

from data.data_frame import tag_model_df
from layout.main_layout import create_layout
from resources.strings import tag_button_names

app = Dash(
    __name__, )
# external_stylesheets=[dbc.themes.MINTY],)

app.layout = create_layout()

tag_buttons_input = []
for item in tag_button_names:
    tag_buttons_input.append(Input(item, 'n_clicks'))


@app.callback(Output('records-data-table', 'data'),
              Output('tag-complete-progress', 'value'),
              Output('selected-row-id', 'value'),
              tag_buttons_input,
              State('records-data-table', 'data'),  # -2
              State('records-data-table', 'active_cell'),  # -1
              )
def on_btn_click(*arg):
    print(f'[on_btn_click]: Start')
    active_cell = arg[-1]
    model = arg[-2]

    if active_cell is None:
        return no_update

    if len(model) == 0:
        return no_update

    print(active_cell)
    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    selected_row_index = model[active_cell['row_id']]['index']

    tag_model_df.at[selected_row_index, 'continent'] = button_id
    no_but_model_df = tag_model_df[~tag_model_df['continent'].str.contains('but')]
    percent_complete = (len(tag_model_df) - len(no_but_model_df)) / len(tag_model_df)
    percent_complete *= 100

    return no_but_model_df.to_dict('records'), percent_complete, active_cell['row_id']


@app.callback(
    Output('left-textarea-example', 'value'),
    Output('right-textarea-example', 'value'),
    Input('records-data-table', 'active_cell'),  # -2
    Input('records-data-table', 'data'),  # -1
)
def update_details(active_cell, data_table):
    print(f'[update_details]: Start')
    print(f'[update_details]: active_cell {active_cell}')
    print(callback_context.triggered[0])

    if active_cell is None:
        return "None", "None"
    # selected_row_index = model[active_cell["row"]]
    row = data_table[active_cell['row_id']]
    return row['country'], row['continent']


# @app.callback(
#     Output(component_id='my-output', component_property='children'),
#     Input(component_id='my-input', component_property='value')
# )
# def update_output_div(input_value):
#     return f'Output: {input_value}'

if __name__ == '__main__':
    app.run_server(debug=True)
