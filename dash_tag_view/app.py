# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# sudo kill $(sudo lsof -t -i:8050)
from dash import Dash
from dash import Input, Output, no_update, callback_context, State
from flask import Flask
from sqlalchemy import create_engine, text

from layout.data_table.layout import tag_data_df
from layout.main_layout import create_layout
from resources.strings import tag_button_names

engine = create_engine('postgresql://postgres:postgres@localhost/test', echo=True)

server = Flask(__name__)

app = Dash(__name__, server=server, suppress_callback_exceptions=False)
# external_stylesheets=[dbc.themes.MINTY],)

app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.server.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/test"

# db = SQLAlchemy(app.server)
# app = DashProxy(prevent_initial_callbacks=True, transforms=[TriggerTransform(), GroupTransform()])

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
    print(f'[on_page_size_change]: End')
    if page_size == 'All':
        return len(tag_data_df)
    return int(page_size)


@app.callback(
    Output('badge', 'children'),
    Output('tag-left-progress', 'value'),
    Input('records-data-table', 'data'),
)
def on_data_change(data):
    # return no_update
    print(f'[on_data_change]: Start')
    nof_tags_left = len(tag_data_df[tag_data_df['tag'].str.contains("Untagged")])
    badge = f'{nof_tags_left} / {len(tag_data_df)}'
    percent_left = nof_tags_left / len(tag_data_df)
    percent_left *= 100
    print(f'[on_data_change]: nof_tags_left: {nof_tags_left}')
    print(f'[on_data_change]: End')
    return badge, percent_left


def get_next_untagged():
    print(f'[get_next_untagged]: Start')
    res = tag_data_df.query('tag ==  "Untagged"').head(1).iloc[0]
    print(f'[get_next_untagged]: res: {res}')
    print(f'[get_next_untagged]: End')
    return res


@app.callback(
    Output('left-textarea-example', 'value'),
    Output('right-textarea-example', 'value'),
    Output('textarea_id', 'value'),
    Output('records-data-table', 'data'),
    Output('records-data-table', 'selected_rows'),
    Output('records-data-table', 'active_cell'),
    tag_buttons_input,
    Input('records-data-table', 'active_cell'),  # -3
    Input('records-data-table', 'selected_rows'),  # -2
    State('records-data-table', 'data'),  # -1
)
def on_tag_click(*args):
    print(f'[on_tag_click]: Start')

    derived_viewport_data = args[-1]
    derived_viewport_selected_rows = args[-2]
    active_cell = args[-3]
    
    print(f'[on_tag_click]: active_cell: {active_cell}')

    if derived_viewport_data is not None:
        print(f'[on_tag_click]: len(derived_viewport_data): {len(derived_viewport_data)}')
    print(f'[on_tag_click]: derived_viewport_selected_rows {derived_viewport_selected_rows}')

    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(f'[on_tag_click]: button_id: {button_id}')

    next_untagged = get_next_untagged()
    tagged_data = tag_data_df[~tag_data_df['tag'].str.contains('Untagged')]

    # handle initial state
    if button_id == "":
        print(f'[on_tag_click]: initial state')
        return next_untagged['comment'], next_untagged['reverse'], str(next_untagged['copy_text']), \
               tagged_data.to_dict('records'), no_update, no_update

    # handle tag button click

    if 'but' in button_id or 'Untagged' in button_id:
        # change current tag (init or not selected)
        if active_cell is None:
            print(f'[on_tag_click]: change current tag')
            tag_table_id = next_untagged['tag_id']
            tag_data_df.at[tag_table_id, 'tag'] = button_id
            next_untagged = get_next_untagged()
            tagged_data = tag_data_df[~tag_data_df['tag'].str.contains('Untagged')]
            return next_untagged['comment'], next_untagged['reverse'], str(next_untagged['copy_text']), \
                   tagged_data.to_dict('records'), no_update, no_update
        else:
            # on selected row
            print(f'[on_tag_click]: selected_rows: {derived_viewport_selected_rows}')
            selected_row = active_cell['row']
            derived_row = derived_viewport_data[selected_row]
            tag_table_id = derived_row['tag_id']
            tag_data_df.at[tag_table_id, 'tag'] = button_id
            tagged_data = tag_data_df[~tag_data_df['tag'].str.contains('Untagged')]
            return next_untagged['comment'], next_untagged['reverse'], str(next_untagged['copy_text']), \
                   tagged_data.to_dict('records'), [], None

    elif button_id == 'records-data-table':
        selected_row = active_cell['row']
        if selected_row < len(derived_viewport_data):
            derived_row = derived_viewport_data[selected_row]
            return derived_row['comment'], derived_row['reverse'], str(derived_row['copy_text']), \
                   no_update, no_update, no_update
        else:
            return no_update

    return no_update





def handle_tag_button(active_cell, button_id, derived_viewport_data):
    print(f'[handle_tag_button]: Start')
    print(f'[on_btn_click]: button_id: {button_id}')
    row = active_cell['row']
    table_id = derived_viewport_data[row]['tag_id']
    print(f'[on_btn_click]: table_id: {table_id}')
    if 'but' in button_id:
        # print(f'[handle_tag_button]: tag_model_df.iloc[table_id]: {tag_model_df.iloc[table_id]}')
        tag_data_df.at[table_id, 'tag'] = button_id

        with engine.begin() as connection:
            tag_data_df.to_sql('test_tsv', con=connection, if_exists='replace')

        # sql_update(button_id, table_id)

        # with engine.begin() as connection:
        #     tag_model_df.to_sql('test_tsv', con=connection, if_exists='replace')

        # postgres_conn = postgres_db.connect()
        # tag_model_df.to_sql('test_tsv', con=postgres_conn, if_exists='replace',
        #                     index=False)
        # postgres_conn.close()
    print(f'[handle_tag_button]: End')


def sql_update(button_id, table_id):
    print(f'[sql_update]: Start')
    with engine.begin() as connection:
        tbl_name = 'test_tsv'
        col_name = 'tag'
        new_val = str(button_id)
        col_id_name = 'tag_id'
        sql_str = f"UPDATE {tbl_name} set {col_name} = '{new_val}'\
            WHERE {col_id_name} = {table_id}"
        print(f'[sql_update]: sql_str: {sql_str}')
        print(f'[sql_update]: text(sql_str): {text(sql_str)}')
        res = connection.execute(text(sql_str))
        print(f'[sql_update]: res: {res}')
    print(f'[sql_update]: End')


# @app.callback(
#     Output('left-textarea-example', 'value'),
#     Output('right-textarea-example', 'value'),
#     Output('textarea_id', 'value'),
#     Input('records-data-table', 'active_cell'),
#     State('records-data-table', 'derived_viewport_data')
# )
# def on_active_cell(active_cell, derived_viewport_data):
#     return no_update
#     print(f'[on_active_cell]: Start')
#
#     print(f'[on_active_cell]: active_cell: {active_cell}')
#     # print(f'[on_active_cell]: derived_viewport_data: {derived_viewport_data}')
#
#     if active_cell is None:
#         print(f'[on_active_cell]: no_update, active_cell is NONE')
#         # update details with first untagged
#         first_untagged = tag_data_df[tag_data_df['tag'].str.contains('Untagged')].head(1)
#         return first_untagged.iloc[0]['comment'], first_untagged.iloc[0]['reverse'], str(first_untagged.iloc[0]['copy_text'])
#         print(f'[on_active_cell]: first_untagged {first_untagged}' )
#
#     if derived_viewport_data is None:
#         print(f'[on_active_cell]: no_update, derived_viewport_data is NONE')
#         return no_update
#
#
#     row = active_cell['row']
#
#     if row < len(derived_viewport_data):
#         row_data = derived_viewport_data[row]
#         print(f'[on_active_cell]: row_data: {row_data}')
#         # print(f"[on_active_cell]: row_data[id]: {row_data['tag_id']}")
#         print(f'[on_active_cell]: End')
#         return row_data['comment'], row_data['reverse'], str(row_data['copy_text'])
#     else:
#         print(f'[on_active_cell]: error: row: {row}, {len(derived_viewport_data)}')
#         return no_update


if __name__ == '__main__':
    app.run_server(debug=True)
