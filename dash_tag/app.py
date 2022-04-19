# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# sudo kill $(sudo lsof -t -i:8050)
from dash import Dash, Input, Output, State, no_update, callback_context

from data.data_frame import tag_model_df
from layout.main_layout import create_layout
from resources.strings import tag_button_names
import dash_bootstrap_components as dbc

app = Dash(
    __name__, )
# external_stylesheets=[dbc.themes.MINTY],)

app.layout = create_layout()

tag_buttons_input = []
for item in tag_button_names:
    tag_buttons_input.append(Input(item, 'n_clicks'))

show_only_tagged = False;


@app.callback(Output('records-data-table', 'data'),
              Output('tag-complete-progress', 'value'),
              Output('table-status-div', 'children'),
              tag_buttons_input,
              Input('show-all', 'n_clicks'),
              Input('show-untagged', 'n_clicks'),
              State('records-data-table', 'active_cell'),  # -2
              State('records-data-table', 'data'), prevent_initial_call=True  # -1
              )
def on_btn_click(*arg):
    print(f'[on_btn_click]: Start')
    global show_only_tagged
    data_table = arg[-1]
    active_cell = arg[-2]

    if len(data_table) == 0:
        return no_update

    if active_cell is None:
        return no_update

    print(f'[on_btn_click]: active_cell: {active_cell}')
    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(f'[on_btn_click]: button_id: {type(button_id)}')

    if button_id == 'show-all':
        show_only_tagged = False
        return tag_model_df.to_dict('records'), no_update, no_update

    selected_row_index = data_table[active_cell['row']]['tag_index']
    print(f'[on_btn_click]: selected_row_index: {selected_row_index}')

    if 'but' in button_id:
        tag_model_df.at[selected_row_index, 'continent'] = button_id

    untagged_model_df = tag_model_df[~tag_model_df['continent'].str.contains('but')]
    untagged_model_df['id'] = range(0, len(untagged_model_df))

    if button_id == 'show-untagged':
        show_only_tagged = True
        return untagged_model_df.to_dict('records'), no_update, no_update

    nof_tags_left = len(untagged_model_df)
    percent_complete = (len(tag_model_df) - nof_tags_left) / len(tag_model_df)
    percent_complete *= 100

    if nof_tags_left > 0:
        alert = dbc.Alert(
            f'Only {len(untagged_model_df)} left, keep up the good work !',
            color='primary',
        )

    else:
        alert = dbc.Alert(
            f'Congratulations ! No more tagging',
            color='success',
        )

    print(f'[on_btn_click]: End')

    if show_only_tagged:
        return tag_model_df.to_dict('records'), percent_complete, alert
    else:
        return untagged_model_df.to_dict('records'), percent_complete, alert


@app.callback(
    Output('left-textarea-example', 'value'),
    Output('right-textarea-example', 'value'),
    Input('records-data-table', 'active_cell'),  # -2
    Input('records-data-table', 'data'), prevent_initial_call=True  # -1
)
def update_details(active_cell, data_table):
    print(f'[update_details]: Start')

    if len(data_table) == 0:
        return "None", "None"

    if active_cell is None:
        return "None", "None"

    print(f'[update_details]: active_cell {active_cell}')

    row = active_cell["row"]
    row_id = active_cell["row_id"]

    # row_index = data_table[row]['index']
    # row_id_index = data_table[row]['index']

    # print(f'[update_details]: row_index {row_index}, row_id_index {row_id_index}')

    row_text = data_table[row_id]
    print(f'[update_details]: End')
    return row_text['country'], row_text['continent']


if __name__ == '__main__':
    app.run_server(debug=True)
