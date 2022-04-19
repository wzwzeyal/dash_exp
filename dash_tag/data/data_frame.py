import pandas as pd

tag_model_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# model_df = model_df.head(5)
tag_model_df['index'] = range(0, len(tag_model_df))

# # using the but string to identify the record was tagged
# current_model_df = tag_model_df.copy()
# current_model_df = tag_model_df[~tag_model_df['continent'].str.contains('but')]
