# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Radio(Component):
    """A Radio component.
Radio component from Material UI

Keyword arguments:
- id (string; optional): The ID of this component.
- checked (boolean; default False): If true, the component is checked.
- checked_timestamp (number; default -1): Timestamp of the last time the component as been clicked on.
- classes (dict; optional): Override or extend the styles applied to the component.
- color (string; optional): The color of the component.
- disabled (boolean; optional): If true, the switch will be disabled.
- disableRipple (boolean; optional): If true, the ripple effect will be disabled.
- label (string; optional): The text to be used in an enclosing label element.
- labelPlacement (string; optional): The position of the label.
- name (string; optional): Name attribute of the input element.
- size (string; optional): The size of the switch.
- style (dict; optional): The style of the switch.
- required (boolean; optional): If true, the input element will be required.
- value (string; optional): The value of the component."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, checked=Component.UNDEFINED, checked_timestamp=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, disableRipple=Component.UNDEFINED, label=Component.UNDEFINED, labelPlacement=Component.UNDEFINED, name=Component.UNDEFINED, size=Component.UNDEFINED, style=Component.UNDEFINED, required=Component.UNDEFINED, value=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'checked', 'checked_timestamp', 'classes', 'color', 'disabled', 'disableRipple', 'label', 'labelPlacement', 'name', 'size', 'style', 'required', 'value']
        self._type = 'Radio'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'checked', 'checked_timestamp', 'classes', 'color', 'disabled', 'disableRipple', 'label', 'labelPlacement', 'name', 'size', 'style', 'required', 'value']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Radio, self).__init__(**args)
