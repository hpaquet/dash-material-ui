import dash_material_ui as dmui
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__,
                external_stylesheets=[
                                "https://fonts.googleapis.com/icon?family=Material+Icons",
                                "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                ])

basic_checkboxes = [
                       dmui.Checkbox(
                           checked=True,
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Checkbox(
                           checked=True,
                           color="primary",
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Checkbox(
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Checkbox(
                           disabled=True,
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Checkbox(
                           checked=True,
                           disabled=True,
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Checkbox(
                           checked=True,
                           indeterminate=True,
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Checkbox(
                           checked=True,
                           color="default",
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Checkbox(
                           checked=True,
                           size="small",
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       )
                   ]


app.layout = html.Div([
                        html.H1('Checkbox'),
                        html.H3('Checkboxes allow the user to select one or more items from a set.'),
                        html.P('Checkboxes can be used to turn an option on or off.'),
                        html.P('If you have multiple options appearing in a list, you can preserve space by using checkboxes instead of on/off switches. If you have a single option, avoid using a checkbox and use an on/off switch instead.'),

                        html.H2('Basic checkboxes'),
                        html.Div(basic_checkboxes),

                        # TODO: Checkbox with FormControlLabel

                        # TODO: Checkboxes with FormGroup

                        # TODO: Label placement

                        # TODO: Customized checkbox

                    ], style={'display': 'inline-block', 'fontFamily': 'Roboto'})


if __name__ == '__main__':
    app.run_server(debug=True)
