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
    Output('tag-complete-progress', 'value'),
    Input('records-data-table', 'data'),
)
def on_data_change(data):
    # return no_update
    print(f'[on_data_change]: Start')
    nof_tags_left = len(tag_data_df[tag_data_df['tag'].str.contains("Untagged")])
    percent_complete = (len(tag_data_df) - nof_tags_left) / len(tag_data_df)
    percent_complete *= 100
    print(f'[on_data_change]: nof_tags_left: {nof_tags_left}')
    print(f'[on_data_change]: End')
    return nof_tags_left, percent_complete


@app.callback(
    Output('records-data-table', 'data'),
    tag_buttons_input,
    Input('text-filter', 'value'),
    State('records-data-table', 'derived_viewport_data'),  # -5
    Input('filter-table', 'value'),  # -4
    State('records-data-table', 'active_cell'),  # -3
    Input('records-data-table', "page_current"),  # -2
    Input('records-data-table', "page_size"),  # -1
)
def update_paged_table(*args):
    print(f'[update_paged_table]: Start')

    page_size = args[-1]
    page_current = args[-2]
    active_cell = args[-3]
    filter_table = args[-4]
    derived_viewport_data = args[-5]
    text_filter = args[-6]
    print(f'[update_paged_table]: page_size: {page_size}')
    # print(f'[update_paged_table]: derived_viewport_data: {derived_viewport_data}')

    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(f'[update_paged_table]: button_id: {button_id}')

    if active_cell is not None:
        print(f'[update_paged_table]: active_cell: {active_cell}')
        # table_id = page_current * page_size +
        if 'but' in button_id:
            row = active_cell['row']
            tag_table_id = derived_viewport_data[row]['tag_id']
            print(f'[update_paged_table]: tag_table_id: {tag_table_id}')
            print(f"[update_paged_table]: before : {tag_data_df.at[tag_table_id, 'tag']}")
            tag_data_df.at[tag_table_id, 'tag'] = button_id
            print(f"[update_paged_table]: after : {tag_data_df.at[tag_table_id, 'tag']}")
            sql_update(button_id, tag_table_id)

    filtered_df = tag_data_df.copy()

    if text_filter is not None:
        if len(text_filter) > 0:
            # https://www.geeksforgeeks.org/get-all-rows-in-a-pandas-dataframe-containing-given-substring/
            filtered_df = filtered_df[filtered_df['tag'].str.contains(text_filter) |
                                      filtered_df['copy_text'].astype(str).str.contains(text_filter) |
                                      filtered_df['random2'].str.contains(text_filter) |
                                      filtered_df['random1'].str.contains(text_filter) |
                                      filtered_df['reverse'].str.contains(text_filter) |
                                      filtered_df['comment'].str.contains(text_filter) |
                                      filtered_df['tag_id'].astype(str).str.contains(text_filter)]

    if filter_table == 1:
        # Only Untagged
        untagged_df = filtered_df[tag_data_df['tag'].str.contains('Untagged')]

        if (page_size == 'All'):
            res = untagged_df.copy()
        else:
            res = untagged_df.iloc[
                  page_current * page_size:(page_current + 1) * page_size
                  ]
    else:
        res = filtered_df.iloc[
              page_current * page_size:(page_current + 1) * page_size
              ]

    # dict(name='Tag', id='tag', ),
    # dict(name='Copy', id='copy_text', ),
    # dict(name="random2", id="random2", ),
    # dict(name="random1", id="random1", ),
    # dict(name='Right Text', id='reverse', ),
    # dict(name='Left Text', id='comment'),
    # dict(name='Tag Id', id='tag_id'),

    return res.to_dict('records')


# @app.callback(
#     Output('records-data-table', 'data'),
#     tag_buttons_input,
#     Input('text-filter', 'value'),  # -4
#     Input('filter-table', 'value'),  # -3
#     State('records-data-table', 'active_cell'),  # -2
#     State('records-data-table', 'derived_viewport_data')  # -1
# )
# def on_btn_click(*args):
#     print(f'[on_btn_click]: Start')
#     print(f'[on_btn_click]: args: {args}')
#
#     text_filter = args[-4]
#     filter_table = args[-3]
#     active_cell = args[-2]
#     derived_viewport_data = args[-1]
#
#     print(f'[on_btn_click]: text_filter: {text_filter}')
#     # print(f'[on_btn_click]: derived_viewport_data: {derived_viewport_data}')
#
#     ctx = callback_context
#     button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#     print(f'[on_btn_click]: button_id: {button_id}')
#
#     if derived_viewport_data is None:
#         print(f'[on_btn_click]: no_update, derived_viewport_data is None')
#         return no_update
#
#     if active_cell is not None:
#         handle_tag_button(active_cell, button_id, derived_viewport_data)
#
#     # dff = tag_model_df.copy()
#     dff = tag_model_df[~tag_model_df['tag'].str.contains('but')]
#
#     print(f'[on_btn_click]: End')
#     # return  no_update
#
#     # if text_filter is not None:
#     #     if len(text_filter) > 0:
#     #         # df = dff[dff['comment'].isin([text_filter])]
#     #         df = dff.filter(like=text_filter, axis=0)
#     #         df = dff.columns.to_series().str.contains(text_filter)
#     #         df = dff[dff['comment'].str.contains(text_filter)]
#     #         # df = dff[dff..str.contains(text_filter)]
#     #         return df.to_dict('records')
#
#     # # identify partial string to look for
#     # keep = ["Wes"]
#     #
#     # # filter for rows that contain the partial string "Wes" in the conference column
#     # df[df.conference.str.contains('|'.join(keep))]
#
#     if filter_table == 2:
#         return tag_model_df.to_dict('records')
#     else:
#         return dff.to_dict('records')


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

    if row < len(derived_viewport_data):
        row_data = derived_viewport_data[row]
        print(f'[on_active_cell]: row_data: {row_data}')
        # print(f"[on_active_cell]: row_data[id]: {row_data['tag_id']}")
        print(f'[on_active_cell]: End')
        return row_data['comment'], row_data['reverse'], str(row_data['copy_text'])
    else:
        print(f'[on_active_cell]: error: row: {row}, {len(derived_viewport_data)}')
        return no_update


if __name__ == '__main__':
    app.run_server(debug=True)
