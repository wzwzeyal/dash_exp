# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# sudo kill $(sudo lsof -t -i:8050)
from dash import Dash, dash_table
from dash import Input, Output, State, no_update, callback_context
from flask import Flask

from data.data_frame import tag_model_df
from layout.main_layout import create_layout
from resources.strings import tag_button_names
from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres:postgres@localhost/test', echo=False)

server = Flask(__name__)

app = Dash(__name__, server=server, suppress_callback_exceptions=True)
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
        return len(tag_model_df)
    return int(page_size)


@app.callback(
    Output('badge', 'children'),
    Output('tag-complete-progress', 'value'),
    Input('records-data-table', 'data'),
)
def on_data_change(data):
    # return no_update
    print(f'[on_data_change]: Start')
    nof_tags_left = len(tag_model_df[tag_model_df['tag'].str.contains("Untagged")])
    percent_complete = (len(tag_model_df) - nof_tags_left) / len(tag_model_df)
    percent_complete *= 100
    print(f'[on_data_change]: nof_tags_left: {nof_tags_left}')
    print(f'[on_data_change]: End')
    return nof_tags_left, percent_complete


@app.callback(
    Output('records-data-table', 'data'),
    tag_buttons_input,
    Input('filter-table', 'value'),
    State('records-data-table', 'active_cell'),  # -2
    Input('records-data-table', 'derived_viewport_data')  # -1
)
def on_btn_click(*args):
    print(f'[on_btn_click]: Start')
    print(f'[on_btn_click]: args: {args}')

    filter_table = args[-3]
    active_cell = args[-2]
    derived_viewport_data = args[-1]
    # print(f'[on_btn_click]: derived_viewport_data: {derived_viewport_data}')

    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(f'[on_btn_click]: button_id: {button_id}')

    if derived_viewport_data is None:
        print(f'[on_btn_click]: no_update, derived_viewport_data is None')
        return no_update

    if active_cell is not None:
        handle_tag_button(active_cell, button_id, derived_viewport_data)

    # dff = tag_model_df.copy()
    dff = tag_model_df[~tag_model_df['tag'].str.contains('but')]

    print(f'[on_btn_click]: End')
    # return  no_update

    if filter_table == 2:
        return tag_model_df.to_dict('records')
    else:
        return dff.to_dict('records')


def handle_tag_button(active_cell, button_id, derived_viewport_data):
    print(f'[handle_tag_button]: Start')
    print(f'[on_btn_click]: button_id: {button_id}')
    row = active_cell['row']
    table_id = derived_viewport_data[row]['tag_id']
    print(f'[on_btn_click]: table_id: {table_id}')
    if 'but' in button_id:
        # print(f'[handle_tag_button]: tag_model_df.iloc[table_id]: {tag_model_df.iloc[table_id]}')
        tag_model_df.at[table_id, 'tag'] = button_id

        sql_update(button_id, table_id)


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
        col_id_name = 'id'
        sql_str = f"UPDATE {tbl_name} set {col_name} = '{new_val}'\
            WHERE {col_id_name} = {table_id}"
        print(f'[sql_update]: sql_str: {sql_str}')
        print(f'[sql_update]: text(sql_str): {text(sql_str)}')
        res = connection.execute(text(sql_str))
        print(f'[sql_update]: res: {res}')
    print(f'[sql_update]: End')


@app.callback(
    Output('left-textarea-example', 'value'),
    Output('right-textarea-example', 'value'),
    Output('textarea_id', 'value'),
    Input('records-data-table', 'active_cell'),
    Input('records-data-table', 'derived_viewport_data')
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
    if row < len(derived_viewport_data):
        row_data = derived_viewport_data[row]
        print(f'[on_active_cell]: row_data: {row_data}')
        print(f'[on_active_cell]: End')
        return row_data['comment'], row_data['reverse'], str(row_data['copy_text'])
    else:
        print(f'[on_active_cell]: error: row: {row}, {len(derived_viewport_data)}')
        return no_update


@app.callback(Output('postgres_datatable', 'children'),
              [Input('interval_pg', 'n_intervals')])
def populate_datatable(n_intervals):
    # global tag_model_df
    # tag_model_df = pd.read_sql_table('test_tsv', con=db.engine)

    return [
        dash_table.DataTable(
            tag_model_df.to_dict('records'),
            # [{"name": i, "id": i} for i in tag_model_df.columns],
            id='records-data-table',
            columns=[
                dict(name='Tag', id='tag', ),
                dict(name='Copy', id='copy_text', ),
                dict(name="random2", id="random2", ),
                dict(name="random1", id="random1", ),
                dict(name='Right Text', id='reverse', ),
                dict(name='Left Text', id='comment', ),
            ],
            page_current=0,
            page_size=1,
            page_action='native',
            style_table={
                'max-height': '400px',
                'overflowY': 'auto'
            },
            # sort_action='native',
            # filter_action='native',
            # editable=True,
            style_data=
            {
                'maxWidth': '150px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },

        ),
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
