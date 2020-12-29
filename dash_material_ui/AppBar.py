# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AppBar(Component):
    """An AppBar component.
AppBar component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the drawer.
- id (string; optional): The ID of this component.
- classes (dict; optional): Override or extend the styles applied to the component.
- color (string; optional): The color of the component.
- palette (dict; optional): Definition of the palettes.
- position (string; optional): The positioning type.
- style (string; optional): The style of the text field."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, palette=Component.UNDEFINED, position=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'classes', 'color', 'palette', 'position', 'style']
        self._type = 'AppBar'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'classes', 'color', 'palette', 'position', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AppBar, self).__init__(children=children, **args)
