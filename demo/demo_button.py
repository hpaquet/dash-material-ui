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

contained_buttons = [
                       dmui.Button(
                           'Default',
                           variant="contained",
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Button(
                           'Primary',
                           color='primary',
                           variant="contained",
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Button(
                           'Secondary',
                           variant="contained",
                           color='secondary',
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Button(
                           'Disabled',
                           variant="contained",
                           disabled=True,
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       ),
                       dmui.Button(
                           'Link',
                           variant="contained",
                           color="primary",
                           href="#contained-buttons",
                           style={'margin': '0.2rem', 'display': 'inline-block'}
                       )
                   ]

disable_elevation = dmui.Button(
                           'Disable elevation',
                           variant="contained",
                           color='primary',
                           disableElevation=True
                       )

text_buttons = [
                   dmui.Button(
                       'Default',
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Button(
                       'Primary',
                       color='primary',
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Button(
                       'Secondary',
                       color='secondary',
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Button(
                       'Disabled',
                       disabled=True,
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Button(
                       'Link',
                       color="primary",
                       href="#contained-buttons",
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   )
               ]

outlined_buttons = [
                   dmui.Button(
                       'Default',
                       variant="outlined",
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Button(
                       'Primary',
                       color='primary',
                       variant="outlined",
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Button(
                       'Secondary',
                       color='secondary',
                       variant="outlined",
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Button(
                       'Disabled',
                       disabled=True,
                       variant="outlined",
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Button(
                       'Link',
                       color="primary",
                       variant="outlined",
                       href="#contained-buttons",
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   )
               ]

size_buttons_0 = [
                  dmui.Button(
                      'Small',
                      size="small",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  ),
                  dmui.Button(
                      'Medium',
                      size="medium",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  ),
                  dmui.Button(
                      'Large',
                      size="large",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  )
              ]

size_buttons_1 = [
                  dmui.Button(
                      'Small',
                      size="small",
                      variant="outlined",
                      color="primary",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  ),
                  dmui.Button(
                      'Medium',
                      size="medium",
                      variant="outlined",
                      color="primary",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  ),
                  dmui.Button(
                      'Large',
                      size="large",
                      variant="outlined",
                      color="primary",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  )
              ]

size_buttons_2 = [
                  dmui.Button(
                      'Small',
                      size="small",
                      variant="contained",
                      color="primary",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  ),
                  dmui.Button(
                      'Medium',
                      size="medium",
                      variant="contained",
                      color="primary",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  ),
                  dmui.Button(
                      'Large',
                      size="large",
                      variant="contained",
                      color="primary",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  )
              ]

size_buttons_3 = [
                  dmui.IconButton(
                      icon='keyboard_arrow_down',
                      size="small",
                      ariaLabel="delete",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  ),
                  dmui.IconButton(
                      icon='delete',
                      size="small",
                      ariaLabel="delete",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  ),
                  dmui.IconButton(
                      icon='delete',
                      size="medium",
                      ariaLabel="delete",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  ),
                  dmui.IconButton(
                      icon='delete',
                      size="large",
                      ariaLabel="delete",
                      style={'margin': '0.2rem', 'display': 'inline-block'}
                  )
              ]

icon_buttons = [
                   dmui.IconButton(
                       icon='delete',
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.IconButton(
                       icon='delete',
                       disabled=True,
                       color='primary',
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.IconButton(
                       icon='alarm',
                       color='secondary',
                       ariaLabel="add an alarm",
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.IconButton(
                       'add_shopping_cart',
                       color='primary',
                       ariaLabel="add to shopping cart",
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   )
               ]

bootstrap_button = {
                 'root': {
                   'boxShadow': 'none',
                   'textTransform': 'none',
                   'fontSize': 16,
                   'padding': '6px 12px',
                   'border': '1px solid',
                   'lineHeight': 1.5,
                   'backgroundColor': '#0063cc',
                   'borderColor': '#0063cc',
                   'fontFamily': ','.join([
                     '-apple-system',
                     'BlinkMacSystemFont',
                     '"Segoe UI"',
                     'Roboto',
                     '"Helvetica Neue"',
                     'Arial',
                     'sans-serif',
                     '"Apple Color Emoji"',
                     '"Segoe UI Emoji"',
                     '"Segoe UI Symbol"',
                   ]),
                   '&:hover': {
                     'backgroundColor': '#0069d9',
                     'borderColor': '#0062cc',
                     'boxShadow': 'none',
                   },
                   '&:active': {
                     'boxShadow': 'none',
                     'backgroundColor': '#0062cc',
                     'borderColor': '#005cbf',
                   },
                   '&:focus': {
                     'boxShadow': '0 0 0 0.2rem rgba(0,123,255,.5)',
                   },
                 },
               }

color_button = {
                  'root': {
                    'color': '#fff',
                    'backgroundColor': '#9c27b0',
                    '&:hover': {
                      'backgroundColor': '#7B1FA2',
                    },
                  },
                }


custom_buttons = [
                   dmui.Button(
                       'Custom CSS',
                       variant="contained",
                       color='primary',
                       customStyle=color_button,
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   ),
                   dmui.Button(
                       'Bootstrap',
                       color='primary',
                       variant="contained",
                       customStyle=bootstrap_button,
                       style={'margin': '0.2rem', 'display': 'inline-block'}
                   )
               ]


app.layout = html.Div([
                        html.H1('Button'),
                        html.H3('Buttons allow users to take actions, and make choices, with a single tap.'),
                        html.P('Buttons communicate actions that users can take. They are typically placed throughout your UI, in places like:'),
                        html.Ul([
                                html.Li('Dialogs'),
                                html.Li('Modal windows'),
                                html.Li('Forms'),
                                html.Li('Cards'),
                                html.Li('Toolbars'),
                        ]),

                        html.H2('Contained Buttons'),
                        html.P('Contained buttons are high-emphasis, distinguished by their use of elevation and fill. They contain actions that are primary to your app.'),
                        html.Div(contained_buttons),
                        html.P('You can remove the elevation with the disableElevation prop.'),
                        html.Div(disable_elevation),

                        html.H2('Text Buttons'),
                        html.P('Text buttons are typically used for less-pronounced actions, including those located:'),
                        html.Ul([
                                html.Li('In dialogs'),
                                html.Li('In cards'),
                        ]),
                        html.P('In cards, text buttons help maintain an emphasis on card content.'),
                        html.Div(text_buttons),

                        html.H2('Outlined Buttons'),
                        html.P('Outlined buttons are medium-emphasis buttons. They contain actions that are important, but aren’t the primary action in an app.'),
                        html.P('Outlined buttons are also a lower emphasis alternative to contained buttons, or a higher emphasis alternative to text buttons.'),
                        html.Div(outlined_buttons),

                        # TODO: Upload button

                        html.H2('Sizes'),
                        html.P('Fancy larger or smaller buttons? Use the size property.'),
                        html.Div(size_buttons_0),
                        html.Div(size_buttons_1),
                        html.Div(size_buttons_2),
                        # html.Div(size_buttons_3),

                        # TODO: Buttons with icons and label

                        html.H2('Icon Buttons'),
                        html.P('Icon buttons are commonly found in app bars and toolbars.'),
                        html.P('Icons are also appropriate for toggle buttons that allow a single choice to be selected or deselected, such as adding or removing a star to an item.'),
                        html.Div(icon_buttons),

                        html.H2('Customized buttons'),
                        html.P('Here are some examples of customizing the component. You can learn more about this in the overrides documentation page.'),
                        html.Div(custom_buttons),

                        # TODO: Complex Buttons

                        # TODO: Limitations

                    ], style={'display': 'inline-block', 'fontFamily': 'Roboto'})


if __name__ == '__main__':
    app.run_server(debug=True)
