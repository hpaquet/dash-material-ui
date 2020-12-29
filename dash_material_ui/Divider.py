# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Divider(Component):
    """A Divider component.
Divider component from Material UI

Keyword arguments:
- id (string; optional): The ID of this component.
- classes (dict; optional): Override or extend the styles applied to the component.
- className (string; optional): Often used with CSS to style elements with common properties.
- absolute (boolean; optional): Absolutely position the element.
- flexItem (boolean; optional): If true, a vertical divider will have the correct height when used in flex container.
- light (boolean; optional): If true, the divider will have a lighter color.
- orientation (string; optional): The divider orientation.
- variant (string; optional): The variant to use.
- palette (dict; optional): Definition of the palettes.
- style (string; optional): The style of the divider."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, classes=Component.UNDEFINED, className=Component.UNDEFINED, absolute=Component.UNDEFINED, flexItem=Component.UNDEFINED, light=Component.UNDEFINED, orientation=Component.UNDEFINED, variant=Component.UNDEFINED, palette=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'classes', 'className', 'absolute', 'flexItem', 'light', 'orientation', 'variant', 'palette', 'style']
        self._type = 'Divider'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'classes', 'className', 'absolute', 'flexItem', 'light', 'orientation', 'variant', 'palette', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Divider, self).__init__(**args)
