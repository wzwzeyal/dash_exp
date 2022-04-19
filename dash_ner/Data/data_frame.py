import pandas as pd

ner_value = ['green', 'red', 'yellow', 'orange']

text_data_df = pd.read_csv('./resources/test.tsv', sep='\t').head(100)[['comment']]

# for data_table row_id
text_data_df['id'] = text_data_df.index
