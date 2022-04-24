import random

import pandas as pd
from dash import dash_table
from dash import html
from sqlalchemy import create_engine

from resources.strings import tag_button_names

predefined_csv = True

use_postgres = False

if predefined_csv:
    print("predefined_csv")
    random1 = ["ABC", "DEF", "GHI"]
    random2 = ["123456", "789012", "0987654"]
    predefined_csv = pd.read_csv('./resources/test.tsv', sep='\t')
    print(predefined_csv.columns)
    predefined_csv = predefined_csv.drop(['Unnamed: 0'], axis=1)
    # print(tag_model_df.columns)
    predefined_csv['tag'] = 'Untagged'
    predefined_csv['tag_id'] = range(0, len(predefined_csv))
    predefined_csv['copy_text'] = range(100000, 100000 + len(predefined_csv))
    predefined_csv['reverse'] = predefined_csv.loc[:, 'comment'].apply(lambda x: x[::-1])
    # https://stackoverflow.com/questions/65982695/insert-a-new-column-in-pandas-with-random-string-values
    predefined_csv['random1'] = pd.Series(random.choices(random1, k=len(predefined_csv)), index=predefined_csv.index)
    predefined_csv['random2'] = pd.Series(random.choices(random2, k=len(predefined_csv)), index=predefined_csv.index)
    print(f'[tag_model_df.to_sql]: Start')
    if use_postgres:
        engine = create_engine('postgresql://postgres:postgres@localhost/test', echo=True)
        with engine.begin() as connection:
            predefined_csv.to_sql('test_tsv', con=connection, if_exists='replace')
        print(f'[tag_model_df.to_sql]: End')

# engine = create_engine('postgresql://postgres:postgres@localhost/test', echo=True)
# with engine.begin() as connection:
#     tag_data_df = pd.read_sql_query("SELECT * FROM test_tsv", con=connection)

if use_postgres:
    tag_data_df = pd.read_sql_table('test_tsv', "postgresql://postgres:postgres@localhost/test")
else:
    tag_data_df = predefined_csv.copy()

print(len(tag_data_df))
# print(tag_data_df.head(10)[['index', 'tag_id']])
tag_data_df.sort_values(by='tag_id', inplace=True)
tag_data_df.set_index('tag_id', inplace=True, drop=False)
print(tag_data_df.columns)
# print(tag_data_df.head(10)[['index', 'tag_id']])

tagged_df = tag_data_df[~tag_data_df['tag'].str.contains('Untagged')]

data_table_layout = html.Div(
    [

        dash_table.DataTable(
            tagged_df.head(10).to_dict('records'),
            # [{"name": i, "id": i} for i in tag_data_df.columns],
            id='records-data-table',
            columns=
            [
                dict(name='Tag', id='tag'),
                dict(name='Copy', id='copy_text', ),
                dict(name="random2", id="random2", ),
                dict(name="random1", id="random1", ),
                dict(name='Right Text', id='reverse', ),
                dict(name='Left Text', id='comment'),
                dict(name='Tag Id', id='tag_id'),
            ],
            page_current=0,
            page_size=10,
            page_action='native',
            style_table={
                'max-height': '400px',
                'overflowY': 'auto'
            },
            sort_action='native',
            filter_action='native',
            row_selectable="single",
            editable=True,
            style_data=
            {
                'maxWidth': '150px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },

        ),

    ],
    style=
    {
        'width': '98%',
        # 'display': 'flex',
        # 'margin-left': '20',
        # 'overflow-y': 'scroll',
    },
)
