# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# sudo kill $(sudo lsof -t -i:8050)
import ast

import dash_bootstrap_components as dbc
from dash import State, ALL, no_update, callback_context, MATCH, Dash, Input, Output

from Data.data_frame import ner_value
from layout.main_layout import create_layout

app = Dash(
    __name__,
)
# external_stylesheets=[dbc.themes.MINTY],)

app.layout = create_layout()

# might be problematic with multiple taggers
ner_input_array = []
selected_indices_set = set()

for count, color in enumerate(ner_value):
    ner_input_array.append(
        Input(color, "n_clicks", )
    )


@app.callback(
    Output({'type': 'button-container', 'index': MATCH}, 'outline'),
    Input({'type': 'button-container', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def on_ner_text_click(_):
    print(f'[on_ner_text_click]: Start')
    global selected_indices_set
    ctx = callback_context
    button_dict = ast.literal_eval(ctx.triggered[0]['prop_id'].split('.')[0])
    print(f'[on_ner_text_click]: ctx.triggered[0]: {ctx.triggered[0]}')
    print(f"[on_ner_text_click]: ctx.triggered[0]: {ctx.triggered[0]['value']})")
    if ctx.triggered[0]['value'] is None:
        print(f'[on_ner_text_click]: no_update')
        print(f'[on_ner_text_click]: End')
        return True
    print(f"[on_ner_text_click]: button_dict' {button_dict}")
    selected_indices_set.add(button_dict['index'])
    print(f'[on_ner_text_click]: selected_indices_set: {selected_indices_set}')
    print(f'[on_ner_text_click]: End')
    return False


@app.callback(
    Output({'type': 'button-container', 'index': ALL}, 'style'),
    ner_input_array,
    prevent_initial_call=True
)
def on_ner_button_click(*args):
    print(f'[on_ner_button_click]: Start')
    global selected_indices_set
    # selected_indices_set.clear()
    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(f'[on_ner_button_click]: button_id: {button_id}')
    print(f'[on_ner_button_click]: selected_indices_set: {selected_indices_set}')
    # print(app.layout.children[1].children[selected_index].style)

    style_res = [no_update] * len(callback_context.outputs_list)
    for index in selected_indices_set:
        style_res[index] = {
            'background-color': "#F5F5F5",
            'color': "black",
            'border': f"2px solid {button_id}",
            'padding': 0,

            # 'background-color': 'light-gray',
        }
    selected_indices_set.clear()
    print(f'[on_ner_button_click]: End')
    return style_res


@app.callback(
    Output('text-button-container', 'children'),
    Input('text-data-table', 'active_cell'),
    State('text-data-table', 'data'),
)
def on_active_cell(active_cell, data):
    print(f'[on_active_cell]: Start')
    if active_cell is not None:
        children = update_text_buttons(active_cell, data)
        # back to school :)
        return children
    print(f'[on_active_cell]: End')
    return no_update


def update_text_buttons(active_cell, data):
    print(f'[update_text_buttons]: Start')
    print(f'[update_text_buttons]: active_cell: {active_cell}')
    text = data[active_cell['row_id']]['comment']
    split_text = text.split(' ')
    print(f'[update_text_buttons]: len(split_text): {len(split_text)}')
    children = []
    print(f"[update_text_buttons]: type(data['row_id']), {type(data[active_cell['row_id']])}")
    for word, value in enumerate(split_text):
        new_button = dbc.Button(
            str(value),

            # for group dynamic callbacks
            id={
                'type': 'button-container',
                'index': word
            },
            # disabled=True,
            className="me-1",
            outline=True,

            style={
                "color": "black",
                # "border": "2px solid #4CAF50",
                # "background-color": "white",
                "padding": 0,
            },
        )
        children.append(new_button)

    # data['row_id']['state'] = children
    print(f'[update_text_buttons]: len(children): {len(children)}')
    print(f'[update_text_buttons]: End')
    return children


if __name__ == '__main__':
    app.run_server(debug=True)
