# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FormControlLabel(Component):
    """A FormControlLabel component.
FormControlLabel component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the component.
- id (string; optional): The ID used to identify this component in Dash callbacks.
- style (dict; optional): Style to apply to the component container.
- checked (boolean; optional): If true, the component is checked.
- customStyle (dict; optional): Custom FormControl style to apply to the component.
- classes (dict; optional): Override or extend the styles applied to the component.
- disabled (boolean; optional): If true, the FormControl will be disabled.
- labelPlacement (string; optional): The position of the label.
- variant (string; optional): The variant to use.
- className (string; optional): Class name to apply to the component."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, checked=Component.UNDEFINED, customStyle=Component.UNDEFINED, classes=Component.UNDEFINED, disabled=Component.UNDEFINED, labelPlacement=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'checked', 'customStyle', 'classes', 'disabled', 'labelPlacement', 'variant', 'className']
        self._type = 'FormControlLabel'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'checked', 'customStyle', 'classes', 'disabled', 'labelPlacement', 'variant', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FormControlLabel, self).__init__(children=children, **args)
