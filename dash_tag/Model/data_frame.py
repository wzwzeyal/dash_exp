import pandas as pd

# model_df = pd.DataFrame(
#     {
#         "Col1": ["aaa", "bbb", "ccc", "ddd"],
#         "Col2": ["123", "456", "789", "012"],
#         "Col3": ["eee", "bbb", "ggg", "hhh"],
#         "Col4": ["a123", "v567", "h765", "d875"],
#     }
# )


tag_model_df = pd.DataFrame() #pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# model_df = model_df.head(5)
tag_model_df['index'] = range(0, len(tag_model_df))


no_but_model_df = tag_model_df.copy()
no_but_model_df = tag_model_df[~tag_model_df['continent'].str.contains('but')]

# table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
