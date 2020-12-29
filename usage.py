import dash_material_ui as dmui
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dmui.AppBar(
        html.Div('hello'),
    )
], style={'display': 'inline-block'})

if __name__ == '__main__':
    app.run_server(debug=True)
