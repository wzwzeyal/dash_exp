import random
import string

import pandas as pd
import psycopg2
from sqlalchemy import create_engine


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


save_data_frame = False

tag_model_df = pd.DataFrame()
# # print(f'[data]: : 1')
# conn_string = "postgresql://postgres:postgres@localhost/test"
# # print(f'[data]: : 2')
# postgres_db = create_engine(conn_string)
# # print(f'[data]: : 3')
# postgres_conn = postgres_db.connect()
# # print(f'[data]: : 4')
# tag_model_df = pd.read_sql_table('test_tsv', con=postgres_db.engine)
# # print(f'[data]: : 5')
# postgres_conn.close()


def save_dataframe():
    global tag_model_df
    random1 = ["ABC", "DEF", "GHI"]
    random2 = ["123456", "789012", "0987654"]
    tag_model_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
    tag_model_df = pd.read_csv('./resources/test.tsv', sep='\t')
    tag_model_df.at[0, 'comment'] = \
        "hkjh lkjh lkjh lkjh lkjh lkjh lkjh lkjh lkjh lkjhljk hljk lkjh\
         lkjhlkjh lkjh kjh lkjh kljh ljkhlkj lkjh lkjh lkjh lkjh lkjh lkhj lkjh lkhl"
    tag_model_df['tag'] = 'Untagged'
    tag_model_df['copy_text'] = range(100000, 100000 + len(tag_model_df))
    tag_model_df['reverse'] = tag_model_df.loc[:, 'comment'].apply(lambda x: x[::-1])
    # https://stackoverflow.com/questions/65982695/insert-a-new-column-in-pandas-with-random-string-values
    tag_model_df['random1'] = pd.Series(random.choices(random1, k=len(tag_model_df)), index=tag_model_df.index)
    tag_model_df['random2'] = pd.Series(random.choices(random2, k=len(tag_model_df)), index=tag_model_df.index)
    # tag_model_df['tag'] = pd.Series(random.choices(tag_button_names, k=len(tag_model_df)), index=tag_model_df.index)
    # tag_model_df['random1'] = np.array([id_generator() for i in range(len(tag_model_df))]).reshape(-1,1)
    # tag_model_df['random2'] = np.array([id_generator() for i in range(len(tag_model_df))]).reshape(-1,1)
    tag_model_df['id'] = range(0, len(tag_model_df))
    tag_model_df = tag_model_df.head(500)
    tag_model_df['tag_index'] = range(0, len(tag_model_df))
    tag_model_df.to_sql('test_tsv', con=postgres_conn, if_exists='replace',
                        index=True, index_label="id2")
    conn = psycopg2.connect(conn_string
                            )
    conn.autocommit = True
    cursor = conn.cursor()
    sql1 = '''select * from data;'''
    cursor.execute(sql1)
    # for i in cursor.fetchall():
    #     print(i)
    # conn.commit()
    conn.close()


if save_data_frame:
    save_dataframe()







