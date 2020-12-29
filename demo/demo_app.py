import dash_material_ui as dmui
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html

from demo.style import theme
from demo.custom_dash import CustomDash

app = CustomDash(__name__,
                external_stylesheets=[
                                "https://fonts.googleapis.com/icon?family=Material+Icons",
                                "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                ])

app_bar_content = [
        dmui.IconButton(
            id='drawer-button-close',
            icon="menu",
            edge="start",
            color="inherit",
            ariaLabel="open drawer",
            className='bar-menu-button',
        ),
        dmui.Typography(
            "Dash Material-UI",
            classes={'root': 'bar-title'},
            variant=theme.h6,
            noWrap=True,
        ),
        html.Div(className='bar-search'),
        html.Div([
            dmui.Icon("search", className='bar-search-icon'),
            dmui.InputBase(
                placeholder="Search…",
                inputProps={'aria-label': 'search'},
                classes={'root': 'bar-input-root', 'input': 'bar-input-input'}
            )],
            className='bar-search'
        ),
        html.Div([
            dmui.IconButton(
                id='email-icon-badge',
                icon="email",
                color="inherit",
                ariaLabel="show 4 new mails",
                badgeContent=4,
                badgeColor='secondary',
            ),
            dmui.IconButton(
                id='notifications-icon-badge',
                icon="notifications",
                color="inherit",
                ariaLabel="show 17 new notifications",
                badgeContent=17,
                badgeColor='secondary',
            ),
            dmui.IconButton(
                icon="account_circle",
                edge="end",
                color="inherit",
                ariaLabel="account of current user",
            ),
        ], className='bar-section-desktop'),
        html.Div([
            dmui.IconButton(
                icon="more_vert",
                color="inherit",
                ariaLabel="show more",
            )
        ], className='bar-section-mobile'),
    ]

app_drawer_content = [
    html.Div(
        dmui.IconButton(
            id='drawer-button-open',
            icon='chevron_left'
        ),
        className="drawer-toolbar"
    ),
    dmui.Divider(),
    dmui.List([
        dmui.ListItem(
            icon='inbox',
            primary='Inbox',
            button=True,
        ),
        dmui.ListItem(
            icon='email',
            primary='Email',
            button=True,
        ),
        dmui.ListItem(
            icon='bookmark',
            primary='Bookmark',
            button=True,
        ),
        dmui.ListItem(
            icon='account_balance',
            primary='Account Balance',
            button=True,
        ),
    ]),
    dmui.Divider(),
    dmui.List([
        dmui.ListItem(
            icon='inbox',
            primary='Inbox',
            button=True,
        ),
        dmui.ListItem(
            icon='email',
            primary='Email',
            button=True,
        ),
        dmui.ListItem(
            icon='bookmark',
            primary='Bookmark',
            button=True,
        )
    ]),
]

app.layout = html.Div([
                        html.Div(
                            dmui.AppBar(
                                children=app_bar_content
                            ),
                            className='bar-root'
                        ),
                        dmui.Drawer(
                            id='main-drawer',
                            children=app_drawer_content,
                            # variant="permanent",
                            open=False
                        ),
                    ])


@app.callback(
    [Output(component_id='main-drawer', component_property='className'),
    Output(component_id='main-drawer', component_property='classes')],
    Input(component_id='main-drawer', component_property='open')
)
def update_output_div(open):
    className = "drawer drawerClose"
    classes = {'paper': 'drawerClose'}

    if open:
        className += "drawer drawerOpen"
        classes = {'paper': 'drawerOpen'}

    return className, classes


@app.callback(
    Output(component_id='main-drawer', component_property='open'),
    [Input(component_id='drawer-button-close', component_property='n_clicks'),
     Input(component_id='drawer-button-open', component_property='n_clicks')],
    State(component_id='main-drawer', component_property='open')
)
def update_output_div(n_click_open, n_click_close, open):
    if n_click_open or n_click_close:
        return not open
    return False


for component_id in ['email-icon-badge', 'notifications-icon-badge']:
    @app.callback(
        Output(component_id=component_id, component_property='badgeContent'),
        [Input(component_id=component_id, component_property='n_clicks')],
        State(component_id=component_id, component_property='badgeContent')
    )
    def update_output_div(n_click, badgeContent):
        if n_click:
            return badgeContent + 1
        return 5  # TODO: add default value


if __name__ == '__main__':
    app.run_server(debug=True)
