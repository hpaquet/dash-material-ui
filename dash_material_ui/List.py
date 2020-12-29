# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class List(Component):
    """A List component.
List component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the list.
- id (string; optional): The ID of this component.
- ariaLabel (a list of or a singular dash component, string or number; optional): Aria-Label of the list.
- classes (dict; optional): Override or extend the styles applied to the component.
- className (string; optional): Often used with CSS to style elements with common properties.
- dense (boolean; optional): If true, compact vertical padding designed for keyboard and mouse input will be used for the list and list items.
- disablePadding (boolean; optional): If true, vertical padding will be removed from the list.
- subheader (a list of or a singular dash component, string or number; optional): The content of the subheader, normally ListSubheader.
- palette (dict; optional): Definition of the palettes."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, ariaLabel=Component.UNDEFINED, classes=Component.UNDEFINED, className=Component.UNDEFINED, dense=Component.UNDEFINED, disablePadding=Component.UNDEFINED, subheader=Component.UNDEFINED, palette=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'ariaLabel', 'classes', 'className', 'dense', 'disablePadding', 'subheader', 'palette']
        self._type = 'List'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'ariaLabel', 'classes', 'className', 'dense', 'disablePadding', 'subheader', 'palette']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(List, self).__init__(children=children, **args)
