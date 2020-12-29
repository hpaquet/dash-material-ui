# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Switch(Component):
    """A Switch component.
Switch component from Material UI

Keyword arguments:
- id (string; optional): The ID of this component.
- checked (boolean; default False): If true, the component is checked.
- checkedIcon (a list of or a singular dash component, string or number; optional): The icon to display when the component is checked.
- classes (dict; optional): Override or extend the styles applied to the component.
- color (string; optional): The color of the component.
- disabled (boolean; optional): If true, the switch will be disabled.
- disableRipple (boolean; optional): If true, the ripple effect will be disabled.
- edge (string; optional): If given, uses a negative margin to counteract the padding on one side.
- icon (a list of or a singular dash component, string or number; optional): The icon to display when the component is unchecked.
- size (string; optional): The size of the switch.
- style (string; optional): The style of the switch.
- value (string; optional): The value of the component."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, checked=Component.UNDEFINED, checkedIcon=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, disableRipple=Component.UNDEFINED, edge=Component.UNDEFINED, icon=Component.UNDEFINED, size=Component.UNDEFINED, style=Component.UNDEFINED, value=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'checked', 'checkedIcon', 'classes', 'color', 'disabled', 'disableRipple', 'edge', 'icon', 'size', 'style', 'value']
        self._type = 'Switch'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'checked', 'checkedIcon', 'classes', 'color', 'disabled', 'disableRipple', 'edge', 'icon', 'size', 'style', 'value']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Switch, self).__init__(**args)
