from dash import html, dcc
import dash_bootstrap_components as dbc

row_details = html.Div(
    [
        dbc.Textarea(id="left-textarea-example", placeholder="1", className="row_text", ),
        dbc.Textarea(id="right-textarea-example", placeholder="2", className="row_text",),

        html.Div(
            [
                html.Span(
                    [
                        "Text1",
                        dcc.Clipboard(
                            target_id="Text1",
                            style={
                                "position": "absolute",
                                "top": 2,
                                "right": 2,
                                "fontSize": 20,
                            },
                        ),
                    ],
                    id="Text1",
                    className="additional_data",
                    style={"position": "relative", }),
                html.Span("Text2", id="Text2", className="additional_data", ),
                html.Span("Text3", id="Text3", className="additional_data", ),

            ],
            id="row_additional_data",
        ),
    ],
    id="row_details",
)