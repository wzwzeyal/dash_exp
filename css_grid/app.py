import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html, dcc

df = pd.DataFrame()  # pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df[' index'] = range(1, len(df) + 1)
app = Dash(__name__)
PAGE_SIZE = 5

row_details = html.Div(
    [

        dbc.Textarea(placeholder="1", style={'border-style': 'none', 'height': '45%'}),
        dbc.Textarea(placeholder="2", style={'border-style': 'none', 'height': '45%'}),

        html.Div(
            [
                # html.Div(
                #     dbc.Textarea(placeholder="3.1", style={'width': '99%', 'height': '87%'}),
                #     style={'flex': '1', 'background-color': 'green'}
                # ),
                # dbc.Textarea(placeholder="3.2", style={'flex': '1'}),
                # dbc.Textarea(placeholder="3.3", id="textarea_id", style={'flex': '1'})
                html.Span(["Text1",
                           dcc.Clipboard(
                               target_id="Text1",
                               style={
                                   "position": "absolute",
                                   "top": 2,
                                   "right": 2,
                                   "fontSize": 20,
                               },
                           ), ],
                          id="Text1",
                          style={'flex': '1', "position": "relative", 'border': '1px solid'}),
                html.Span("Text2", style={'flex': '1', 'border': '1px solid'}, ),
                html.Span("Text3", style={'flex': '1', 'border': '1px solid'}),

            ],
            # style={'display': 'grid', 'grid-auto-flow': 'column', 'grid-auto-columns': '1fr'},
            style={'display': 'flex', 'gap': '10px', 'height': '7%', 'align-content': 'start'}
        ),
    ],
    style={'display': 'flex', 'flex-direction': 'column', 'height': '100%', 'width': '96%',
           'margin-left': '2%'}
)
lst = []
for item in range(20):
    lst.append(
        dbc.Button(
            item,
            id=str(item),
            outline=True,
            style={
                # "width": "120px",
                "color": 'black',
                'border': 'groove',
                # "padding": "5px",
                "margin-right": 5,
                "margin-bottom": 3,
                "display": "inline",
                # "background-color": "white",
            }),
    )

buttons_array = html.Div(
    [
        html.Div(
            lst[:10],
            style={'border-style': 'none', 'height': '65%', 'margin-top': '10px'}

        ),
        html.Div(
            lst[10:],
            style={'border-style': 'none', 'height': '35%', 'margin-top': '10px'}
        ),
    ],
    # [
    #     # dbc.Textarea(placeholder="1", style={'border-style': 'none', 'height': '50%'}),
    #
    #     dbc.Textarea(placeholder="2", style={'border-style': 'none', 'height': '50%'}),
    # ],
    style={'display': 'flex', 'flex-direction': 'column', 'height': '100%'}
)

main_layout = html.Div(
    [
        html.Div([row_details], style={'width': '70%', }),
        html.Div(
            style={
                'border': '2px solid #eff2f5',
                'margin-top': '2%',
                'height': '89%',
                'margin-right': '10px'
            }),
        html.Div([buttons_array], style={'width': '30%', }),
    ],
    style={
        'display': 'flex',
        'background-color': '#ffffff',
        'height': '100%',
        # 'margin-left': '2%',
        # 'margin-bottom': '2%',
        # 'width': '95%',
        # 'margin-left': '20px',
    }
)

status_layout = html.Div(
    [
        html.Div(
            [
                html.Span(
                    'Tagged texts: '
                ),
                html.B(
                    "45",
                    id="nof-tagged-texts",
                    style={},
                ),
                html.Span(
                    " out of "
                ),
                html.Span(
                    "1000",
                    id="nof-total-texts"
                ),
            ],
        ),

        dbc.Progress(
            id='tag-left-progress',
            value=100,
            style=
            {
                'margin-left': '2em',
                # 'height': 20,
                # 'border': 'groove',
                'width': '60%',
                'height': '5px'
            },
        ),
    ],
    style={'display': 'flex', 'align-items': 'center'}
)

table_layout = html.Div("table_layout", style={'height': '20px', 'background-color': 'red'})

app.layout = html.Div(
    [
        html.Div("Tag Data", style={'height': '5%', 'width': '95%', 'margin-left': '2%'}),
        html.Div([main_layout], style={'height': '70%', 'width': '95%', 'margin-left': '2%'}),
        html.Div([status_layout], style={'height': '5%', 'width': '95%', 'margin-left': '2%'}),
        html.Div([table_layout], style={'height': '20%', 'width': '95%', 'margin-left': '2%'}),
    ],
    id='body',
    style={
        # 'display': 'flex',
        # 'flex-direction': 'column',
        'background-color': '#eff2f5',
        # 'flex-grow': '1',

        'position': 'absolute',
        'top': 0,
        'bottom': 0,
        'height': '100%',
        'width': '100%',
    }
)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
