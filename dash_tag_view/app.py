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
    Output('records-data-table', 'active_cell'),
    tag_buttons_input,
    Input('records-data-table', 'active_cell'),  # -2
    State('records-data-table', 'data'),  # -1
)
def on_tag_click(*args):
    print(f'[on_tag_click]: Start')

    data = args[-1]
    active_cell = args[-2]

    print(f'[on_tag_click]: active_cell: {active_cell}')

    if data is not None:
        print(f'[on_tag_click]: len(data): {len(data)}')

    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(f'[on_tag_click]: button_id: {button_id}')

    next_untagged = get_next_untagged()
    tagged_data = tag_data_df[~tag_data_df['tag'].str.contains('Untagged')]

    output_res = no_update

    # handle initial state
    if button_id == "":
        print(f'[on_tag_click]: initial state')
        output_res = (
            next_untagged['comment'],
            next_untagged['reverse'],
            str(next_untagged['copy_text']),
            tagged_data.to_dict('records'),
            no_update)
        return output_res

    # handle tag button click

    if 'but' in button_id or 'Untagged' in button_id:
        # change current tag (init or not selected)
        if active_cell is None:
            print(f'[on_tag_click]: change current tag')
            tag_table_id = next_untagged['tag_id']
            tag_data_df.at[tag_table_id, 'tag'] = button_id
            next_untagged = get_next_untagged()
            tagged_data = tag_data_df[~tag_data_df['tag'].str.contains('Untagged')]
            output_res = (next_untagged['comment'], next_untagged['reverse'], str(next_untagged['copy_text']), \
                           tagged_data.to_dict('records'), no_update)
        else:
            # on selected row
            selected_row = active_cell['row']
            print(f'[on_tag_click]: selected_row: {selected_row}')
            derived_row = data[selected_row]
            tag_table_id = derived_row['tag_id']
            tag_data_df.at[tag_table_id, 'tag'] = button_id
            tagged_data = tag_data_df[~tag_data_df['tag'].str.contains('Untagged')]
            output_res = (next_untagged['comment'], next_untagged['reverse'], str(next_untagged['copy_text']), \
                   tagged_data.to_dict('records'), None)

    elif button_id == 'records-data-table':
        selected_row = active_cell['row']
        if selected_row < len(data):
            derived_row = data[selected_row]
            output_res = (derived_row['comment'], derived_row['reverse'], str(derived_row['copy_text']), \
                   no_update, no_update)

    return output_res


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


if __name__ == '__main__':
    app.run_server(debug=True)
