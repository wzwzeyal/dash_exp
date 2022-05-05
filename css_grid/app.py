import pandas as pd
from dash import Dash, html

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

df[' index'] = range(1, len(df) + 1)

app = Dash(__name__)

PAGE_SIZE = 5

app.layout = html.Div(
    [
        html.Div(
            "Header",
            style={
                'grid-column-start': '1',
                'grid-column-end': '13',
            }
        ),
        html.Div('Side nav',
                 style=
                 {
                     'grid-column-start': '1',
                     'grid-column-end': '5',

                 }
                 ),
        html.Div(
            [
                html.Div('Intro'),
                html.Div('Cake'),
                html.Div('Cake'),
                html.Div('Cake'),
            ],
            style=
            {
                'grid-column-start': '5',
                'grid-column-end': '13',
                # 'grid-row-start': '2',
                # 'grid-row-end': '4',
                'grid-row': '2 / 4',
            }
        ),
        html.Div(
            'Aside',
            style=
            {
                'grid-column-start': '1',
                'grid-column-end': '5',
            }
        ),
        html.Div(
            'Footer',
            style={
                'grid-column-start': '1',
                'grid-column-end': '13',
            }
        ),

    ],
    id='body',
    style={
        'margin': '1em',
        'display': 'grid',
        'grid': 'auto-flow min-content / repeat(12, 1fr)',
        'grid-gap': '1em'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
