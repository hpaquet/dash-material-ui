import dash_material_ui as dmui
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output, State, ALL
import dash_html_components as html

app = dash.Dash(__name__,
                external_stylesheets=[
                                "https://fonts.googleapis.com/icon?family=Material+Icons",
                                "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                ])

standalone_radio = [
                       dmui.Radio(
                           checked=False,
                           value="a",
                           id={'type': 'standalone-radio','index': 'a'},
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Radio(
                           checked=False,
                           value="b",
                           color="primary",
                           id={'type': 'standalone-radio','index': 'b'},
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Radio(
                           checked=False,
                           value="c",
                           id={'type': 'standalone-radio','index': 'c'},
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Radio(
                           checked=False,
                           value="d",
                           color="default",
                           id={'type': 'standalone-radio','index': 'd'},
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Radio(
                           checked=False,
                           value="e",
                           color="default",
                           size="small",
                           id={'type': 'standalone-radio','index': 'e'},
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       )
                   ]

label_radio = [
                   dmui.Radio(
                       checked=False,
                       value="top",
                       color="primary",
                       # id={'type': 'standalone-radio','index': 'a'},
                       label="Top",
                       labelPlacement="top",
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Radio(
                       checked=False,
                       value="start",
                       color="primary",
                       label="Start",
                       labelPlacement="start",
                       # id={'type': 'standalone-radio','index': 'b'},
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Radio(
                       checked=False,
                       value="c",
                       # id={'type': 'standalone-radio','index': 'c'},
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Radio(
                       checked=False,
                       value="d",
                       color="default",
                       # id={'type': 'standalone-radio','index': 'd'},
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Radio(
                       checked=False,
                       value="e",
                       color="default",
                       size="small",
                       # id={'type': 'standalone-radio','index': 'e'},
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   )
               ]


app.layout = html.Div([
                        html.H1('Radio'),
                        html.H3('Radio buttons allow the user to select one option from a set.'),
                        html.P('Use radio buttons when the user needs to see all available options. If available options can be collapsed, consider using a dropdown menu because it uses less space.'),
                        html.P('Radio buttons should have the most commonly used option selected by default.'),

                        html.H2('RadioGroup'),
                        html.P('RadioGroup is a helpful wrapper used to group Radio components that provides an easier API, and proper keyboard accessibility to the group.'),
                        # html.Div(group_radio),

                        html.H2('Standalone radio buttons'),
                        html.P('Radio can also be used standalone, without the RadioGroup wrapper.'),
                        html.Div(standalone_radio),

                        html.H2('Label placement'),
                        html.P('You can change the placement of the label with the FormControlLabel component\'s labelPlacement prop:'),
                        html.Div(label_radio),

                    ], style={'display': 'inline-block', 'fontFamily': 'Roboto'})


@app.callback(
    Output({'type': 'standalone-radio', 'index': ALL}, 'checked'),
    Input({'type': 'standalone-radio', 'index': ALL}, 'checked_timestamp'),
    State({'type': 'standalone-radio', 'index': ALL}, 'checked'),
)
def display_output(checked_timestamp, checked):

    ctx = dash.callback_context

    if ctx.triggered[0]['value']:
        checked = [False if ts != ctx.triggered[0]['value'] else True for ts in checked_timestamp]

    return checked


if __name__ == '__main__':
    app.run_server(debug=True)
