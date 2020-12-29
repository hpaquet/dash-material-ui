# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Checkbox(Component):
    """A Checkbox component.
Checkbox component from Material UI

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- style (dict; optional): Style to apply to the component container.
- customStyle (dict; optional): Custom checkbox style to apply to the component.
- checked (boolean; default False): If true, the component is checked.
- checkedIcon (a list of or a singular dash component, string or number; optional): The icon to display when the component is checked.
- classes (dict; optional): Override or extend the styles applied to the component.
- color (string; optional): The color of the component.
- disabled (boolean; optional): If true, the checkbox will be disabled.
- disableRipple (boolean; optional): If true, the ripple effect will be disabled.
- icon (a list of or a singular dash component, string or number; optional): The icon to display when the component is unchecked.
- indeterminate (boolean; optional): If true, the component appears indeterminate.
- indeterminateIcon (a list of or a singular dash component, string or number; optional): The icon to display when the component is indeterminate.
- size (string; optional): The size of the checkbox.
- value (dict; optional): The value of the component.
- className (string; optional): Class name to apply to the component."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, customStyle=Component.UNDEFINED, checked=Component.UNDEFINED, checkedIcon=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, disableRipple=Component.UNDEFINED, icon=Component.UNDEFINED, indeterminate=Component.UNDEFINED, indeterminateIcon=Component.UNDEFINED, size=Component.UNDEFINED, value=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'style', 'customStyle', 'checked', 'checkedIcon', 'classes', 'color', 'disabled', 'disableRipple', 'icon', 'indeterminate', 'indeterminateIcon', 'size', 'value', 'className']
        self._type = 'Checkbox'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'style', 'customStyle', 'checked', 'checkedIcon', 'classes', 'color', 'disabled', 'disableRipple', 'icon', 'indeterminate', 'indeterminateIcon', 'size', 'value', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Checkbox, self).__init__(**args)
