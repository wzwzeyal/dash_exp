import pandas as pd

tag_model_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
tag_model_df['id'] = range(0, len(tag_model_df))
tag_model_df = tag_model_df.head(13)
tag_model_df['tag_index'] = range(0, len(tag_model_df))

