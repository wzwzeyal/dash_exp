# All my tutorials on https://www.youtube.com/channel/UCqBFsuAz41sqWcFjZkqmJqQ/featured
import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html


import psycopg2
import pandas as pd
from sqlalchemy import create_engine

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# app requires "pip install psycopg2" as well

server = Flask(__name__)
app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True)
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# for your home PostgreSQL test table
app.server.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/test"

conn_string = app.server.config["SQLALCHEMY_DATABASE_URI"]
# for your live Heroku PostgreSQL database
# app.server.config["SQLALCHEMY_DATABASE_URI"] = "postgres://kcfwfqwznavpjq:9473936daf43bff3d17c1dd8ab2c28144dfbf677\
# 14cb30622e3017bbe55cdeac@ec2-34-197-188-147.compute-1.amazonaws.com:5432/d9eat64jon4dti"

db = SQLAlchemy(app.server)

db = create_engine(conn_string)
conn = db.connect()

# our dataframe
data = {'Name': ['Tom', 'dick', 'harry'],
        'Age': [22, 21, 24]}

# Create DataFrame
df = pd.read_csv('./resources/test.tsv', sep='\t')
df.to_sql('test_tsv', con=conn, if_exists='replace',
          index=False)
conn = psycopg2.connect(conn_string
                        )
conn.autocommit = True
cursor = conn.cursor()

sql1 = '''select * from data;'''
cursor.execute(sql1)
for i in cursor.fetchall():
    print(i)

# conn.commit()
conn.close()



app.layout = html.Div([
    html.Div([
        dcc.Input(
            id='adding-rows-name',
            placeholder='Enter a column name...',
            value='',
            style={'padding': 10}
        ),
        html.Button('Add Column', id='adding-columns-button', n_clicks=0)
    ], style={'height': 50}),

    dcc.Interval(id='interval_pg', interval=86400000*7, n_intervals=0),  # activated once/week or when page refreshed
    html.Div(id='postgres_datatable'),

    html.Button('Add Row', id='editing-rows-button', n_clicks=0),
    html.Button('Save to PostgreSQL', id='save_to_postgres', n_clicks=0),

    # Create notification when saving to excel
    html.Div(id='placeholder', children=[]),
    dcc.Store(id="store", data=0),
    dcc.Interval(id='interval', interval=1000),

    dcc.Graph(id='my_graph')

])



if __name__ == '__main__':
    app.run_server(debug=True)