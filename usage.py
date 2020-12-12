import dash_material_ui as dmui
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dmui.Button(
        id='button-0',
        variant="contained",
        children='Default',
        style={'margin': '0.2rem', 'display': 'inline-block'}
    ),
    dmui.Button(
        id='button-1',
        children='Primary',
        color='primary',
        style={'margin': '0.2rem', 'display': 'inline-block'}
    ),
    dmui.Button(
        id='button-2',
        variant="outlined",
        children='Secondary',
        color='secondary',
        style={'margin': '0.2rem', 'display': 'inline-block'}
    ),
    dmui.Button(
        id='button-3',
        variant="contained",
        children='Disabled',
        size='large',
        disabled=True,
        style={'margin': '0.2rem', 'display': 'inline-block'}
    ),
    dmui.Button(
        id='button-4',
        variant="contained",
        children='Link',
        color="primary",
        href="#contained-buttons",
        disableElevation=True,
        style={'margin': '0.2rem', 'display': 'inline-block'}
    )
], style={'display': 'inline-block'})

if __name__ == '__main__':
    app.run_server(debug=True)
