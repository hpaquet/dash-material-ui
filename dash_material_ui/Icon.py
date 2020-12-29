# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Icon(Component):
    """An Icon component.
Icon component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the drawer.
- id (string; optional): The ID of this component.
- classes (dict; optional): Override or extend the styles applied to the component.
- className (string; optional): Often used with CSS to style elements with common properties.
- color (string; optional): The color of the component.
- fontSize (string; optional): The fontSize applied to the icon.
- palette (dict; optional): Definition of the palettes.
- style (string; optional): The style of the text field."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, classes=Component.UNDEFINED, className=Component.UNDEFINED, color=Component.UNDEFINED, fontSize=Component.UNDEFINED, palette=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'classes', 'className', 'color', 'fontSize', 'palette', 'style']
        self._type = 'Icon'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'classes', 'className', 'color', 'fontSize', 'palette', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Icon, self).__init__(children=children, **args)
