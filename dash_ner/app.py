# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# sudo kill $(sudo lsof -t -i:8050)
import numpy as np
from dash import Dash
import ast
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, MATCH, ALL, no_update, callback_context

from Model.data_frame import ner_value
from view.layout import create_layout
import pandas as pd

app = Dash(
    __name__, )
# external_stylesheets=[dbc.themes.MINTY],)

app.layout = create_layout()

# might be problematic with multiple taggers
input_array = []
output_array = []
style_array = []
ner_input_array = []
selected_indices_set = set()


for count, color in enumerate(ner_value):
    ner_input_array.append(
        Input(color, "n_clicks", )
    )

for count in range(200):
    input_array.append(
        Input(str(count), "n_clicks", )
    )
    output_array.append(
        Output(str(count), "style")
    )
    style_array.append(
        {
            "color": "black",
            # "border": "2px solid #4CAF50",
            # "background-color": "white",
            "padding": 0,
        }
    )


@app.callback(
    Output('container', 'children'),
    # Output({'type': 'button-container', 'index': MATCH}, 'value'),
    Input({'type': 'button-container', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def on_ner_text_click(values):
    # print(values)
    # print(f'triggered: {callback_context.triggered}')
    # return no_update
    print('on_ner_text_click')
    global selected_indices_set
    ctx = callback_context
    button_dict = ast.literal_eval(ctx.triggered[0]['prop_id'].split('.')[0])
    print(ctx.triggered[0])
    print(ctx.triggered[0]['value'])
    if ctx.triggered[0]['value'] is None:
        print("no_update")
        return no_update
    print(button_dict['index'])
    selected_indices_set.add(button_dict['index'])
    print(selected_indices_set)
    # if isinstance(button_id, str):
    #     if len(button_id) > 0:
    #         selected_indices.append(int(button_id))
    #         print(f'[on_ner_click]: selected_indices: {selected_indices}')
    return no_update


@app.callback(
    Output({'type': 'button-container', 'index': ALL}, 'style'),
    ner_input_array,
    prevent_initial_call=True
)
def on_ner_button_click(*args):
    print('on_ner_button_click')
    global selected_indices_set
    # selected_indices_set.clear()
    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(button_id)

    print(f'selected_indices {type(selected_indices_set)}, value: {selected_indices_set}')
    # print(app.layout.children[1].children[selected_index].style)

    res = [no_update] * len(callback_context.outputs_list)
    for index in selected_indices_set:
        style_array[index] = dict(
            color="black",
            border=f"2px solid {button_id}",
            padding=0
        )
        res[index] = dict(
            color="black",
            border=f"2px solid {button_id}",
            padding=0
        )
    selected_indices_set.clear()
    return res



@app.callback(
    Output('text-button-container', 'children'),
    Input('model', 'active_cell'),
    State('model', 'data'),
    State('text-button-container', 'children')
)
def on_active_cell(active_cell, data, children):
    if active_cell is not None:
        # print(active_cell['row'])
        text = data[active_cell['row']]['comment']
        split_text = text.split(' ')

        children.clear()

        for count, value in enumerate(split_text):
            new_button = dbc.Button(
                str(value),
                id={
                    'type': 'button-container',
                    'index': count
                },
                # id=str(count),
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
        return children
    return no_update


if __name__ == '__main__':
    app.run_server(debug=True)
