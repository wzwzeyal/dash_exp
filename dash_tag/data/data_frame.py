import pandas as pd
import numpy as np

import string
import random

random1 = ["ABC", "DEF", "GHI"]
random2 = ["123456", "789012", "0987654"]

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

tag_model_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

tag_model_df = pd.read_csv('./resources/test.tsv', sep='\t')
tag_model_df['tag'] = 'Untagged'
tag_model_df['copy_text'] = range(100000, 100000 + len(tag_model_df))
tag_model_df['reverse'] = tag_model_df.loc[:,'comment'].apply(lambda x: x[::-1])

# https://stackoverflow.com/questions/65982695/insert-a-new-column-in-pandas-with-random-string-values


tag_model_df['random1'] = pd.Series(random.choices(random1, k=len(tag_model_df)), index=tag_model_df.index)
tag_model_df['random2'] = pd.Series(random.choices(random2, k=len(tag_model_df)), index=tag_model_df.index)

# tag_model_df['random1'] = np.array([id_generator() for i in range(len(tag_model_df))]).reshape(-1,1)
# tag_model_df['random2'] = np.array([id_generator() for i in range(len(tag_model_df))]).reshape(-1,1)

tag_model_df['id'] = range(0, len(tag_model_df))
tag_model_df = tag_model_df.head(500)
tag_model_df['tag_index'] = range(0, len(tag_model_df))

