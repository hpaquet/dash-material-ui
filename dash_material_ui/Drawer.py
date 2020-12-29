# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Drawer(Component):
    """A Drawer component.
Drawer component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the drawer.
- id (string; optional): The ID of this component.
- classes (dict; optional): Override or extend the styles applied to the component.
- className (string; optional): Often used with CSS to style elements with common properties.
- anchor (string; optional): Side from which the drawer will appear.
- elevation (number; optional): The elevation of the drawer.
- open (boolean; optional): If true, the drawer is open.
- transitionDuration (number; optional): The duration for the transition, in milliseconds.
- style (string; optional): The style of the text field.
- variant (string; optional): The variant to use.
- palette (dict; optional): Definition of the palettes."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, classes=Component.UNDEFINED, className=Component.UNDEFINED, anchor=Component.UNDEFINED, elevation=Component.UNDEFINED, open=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, style=Component.UNDEFINED, variant=Component.UNDEFINED, palette=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'classes', 'className', 'anchor', 'elevation', 'open', 'transitionDuration', 'style', 'variant', 'palette']
        self._type = 'Drawer'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'classes', 'className', 'anchor', 'elevation', 'open', 'transitionDuration', 'style', 'variant', 'palette']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Drawer, self).__init__(children=children, **args)
