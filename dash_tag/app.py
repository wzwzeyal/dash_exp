# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# sudo kill $(sudo lsof -t -i:8050)
import numpy as np
from dash import Dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, MATCH, ALL, no_update, callback_context

from Model.data_frame import model_df
from resources.strings import items_list
from view.layout import create_layout
import pandas as pd

app = Dash(
    __name__, )
# external_stylesheets=[dbc.themes.MINTY],)

app.layout = create_layout()

input_callback = []
for item in items_list:
    input_callback.append(Input(item, 'n_clicks'))



@app.callback(Output('container', 'children'),
              Output('model', 'data'),
              Output('model', 'selected_rows'),
              Output('but-complete', 'value'),
              input_callback,
              State('model', 'data'),  # -2
              State('model', 'selected_rows'),  # -1
              )
def on_btn_click(*arg):
    selected_row_ids = arg[-1]
    model = arg[-2]

    if selected_row_ids is None:
        return no_update

    if len(model) == 0:
        return  no_update

    print(selected_row_ids)
    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if len(selected_row_ids) == 1:
        if type(selected_row_ids[0]) == int:
            selected_row_index = model[selected_row_ids[0]]['index']
            # row_model = model[selected_row_id]
            # print(row_model)
            # row_model['continent'] = button_id

            model_df.at[selected_row_index, 'continent'] = button_id
            no_but_model_df = model_df[~model_df['continent'].str.contains('but')]
            percent_complete = (len(model_df) - len(no_but_model_df)) / len(model_df)
            percent_complete *= 100

            # model_df.iloc[selected_row_id]['continent'] = button_id
            # print(type(model))
            return button_id, no_but_model_df.to_dict('records'), selected_row_ids, percent_complete  # model_df.to_dict('records')

    # if selected_row_id != np.nan:
    #     print(model_df.iloc[selected_row_id])

    return no_update


@app.callback(
    Output('left-textarea-example', 'value'),
    Output('right-textarea-example', 'value'),
    Output('selected-row-id', 'value'),
    Input('model', 'selected_rows'),
    State('model', 'data'),
)
def update_details(table_selected_rows, model):
    if table_selected_rows is None:
        return "None", "None", np.nan
    if len(table_selected_rows) == 1:
        if len(model) > 0:
            selected_row_index = model[table_selected_rows[0]]['index']
            row = model_df.iloc[selected_row_index]
            return row['country'], row['continent'], row['index']
    return no_update, no_update, no_update


# @app.callback(
#     Output(component_id='my-output', component_property='children'),
#     Input(component_id='my-input', component_property='value')
# )
# def update_output_div(input_value):
#     return f'Output: {input_value}'

if __name__ == '__main__':
    app.run_server(debug=True)
