# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# sudo kill $(sudo lsof -t -i:8050)
from dash import Dash
from dash import Input, Output, State, no_update, callback_context

from dash_tag_view.data.data_frame import tag_model_df
from layout.main_layout import create_layout
from resources.strings import tag_button_names

app = Dash(
    __name__, )
# external_stylesheets=[dbc.themes.MINTY],)

app.layout = create_layout()

tag_buttons_input = []
for item in tag_button_names:
    tag_buttons_input.append(
        Input(item, 'n_clicks'))


@app.callback(
    Output('records-data-table', 'page_size'),
    Input('page_size', 'value'),
)
def on_page_size_change(page_size):
    print(f'[on_page_size_change]: Start')
    print(f'[on_page_size_change]: page_size: {page_size}')
    return page_size
    print(f'[on_page_size_change]: End')



@app.callback(
    Output('badge', 'children'),
    Input('records-data-table', 'data'),
)
def on_data_change(data):
    print(f'[on_data_change]: Start')
    nof_tags_left = len(tag_model_df[tag_model_df['tag'].str.contains("Untagged")])
    print(f'[on_data_change]: nof_tags_left: {nof_tags_left}')
    print(f'[on_data_change]: End')
    return nof_tags_left
    
    return  no_update

@app.callback(
    Output('records-data-table', 'data'),
    tag_buttons_input,
    State('records-data-table', 'active_cell'),
    State('records-data-table', 'derived_viewport_data')  # -1
)
def on_btn_click(*args):
    print(f'[on_btn_click]: Start')
    print(f'[on_btn_click]: args: {args}')

    active_cell = args[-2]
    derived_viewport_data = args[-1]
    print(f'[on_btn_click]: derived_viewport_data: {derived_viewport_data}')

    if active_cell is None:
        print(f'[on_btn_click]: no_update, active_cell is None')
        return no_update

    if derived_viewport_data is None:
        print(f'[on_btn_click]: no_update, derived_viewport_data is None')
        return no_update

    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    handle_tag_button(active_cell, button_id, derived_viewport_data)
    return tag_model_df.to_dict('records')

    print(f'[on_btn_click]: End')
    return no_update


def handle_tag_button(active_cell, button_id, derived_viewport_data):
    print(f'[handle_tag_button]: Start')
    print(f'[on_btn_click]: button_id: {button_id}')
    row = active_cell['row']
    table_id = derived_viewport_data[row]['id']
    print(f'[on_btn_click]: table_id: {table_id}')
    tag_model_df.at[table_id, 'tag'] = button_id
    print(f'[handle_tag_button]: End')


@app.callback(
    Output('left-textarea-example', 'value'),
    Output('right-textarea-example', 'value'),
    Output('textarea_id', 'value'),
    Input('records-data-table', 'active_cell'),
    State('records-data-table', 'derived_viewport_data')
)
def on_active_cell(active_cell, derived_viewport_data):
    print(f'[on_active_cell]: Start')

    print(f'[on_active_cell]: active_cell: {active_cell}')
    # print(f'[on_active_cell]: derived_viewport_data: {derived_viewport_data}')

    if active_cell is None:
        print(f'[on_active_cell]: no_update, active_cell is NONE')
        return no_update

    if derived_viewport_data is None:
        print(f'[on_active_cell]: no_update, derived_viewport_data is NONE')
        return no_update

    row = active_cell['row']
    row_data = derived_viewport_data[row]
    print(f'[on_active_cell]: row_data: {row_data}')
    print(f'[on_active_cell]: End')
    return row_data['comment'], row_data['reverse'], str(row_data['copy_text'])


if __name__ == '__main__':
    app.run_server(debug=True)
