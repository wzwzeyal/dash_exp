from dash import Dash
import dash_bootstrap_components as dbc
from dash import dcc, html

app = Dash(
    __name__, )

app.layout = html.Div(
    [
        dbc.Button("Button1", style={'width': '10%'}, outline=True, color="warning"),

        dbc.Button("Button2", style={'width': '10%'}),

        dbc.Textarea("Text", style={'width': '30%'}),

    ], style={'display': 'flex', 'gap': '5px', 'margin': '10px', }  # className="flex-container",
)

if __name__ == '__main__':
    app.run_server(debug=True)
