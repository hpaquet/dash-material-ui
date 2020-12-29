# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FormLabel(Component):
    """A FormLabel component.
FormLabel component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the component.
- id (string; optional): The ID used to identify this component in Dash callbacks.
- style (dict; optional): Style to apply to the component container.
- component (string; optional): The component used for the root node.
- customStyle (dict; optional): Custom FormLabel style to apply to the component.
- classes (dict; optional): Override or extend the styles applied to the component.
- color (string; optional): The color of the component.
- disabled (boolean; optional): If true, the FormLabel will be disabled.
- error (boolean; optional): If true, the label should be displayed in an error state.
- filled (boolean; optional): If true, the label should use filled classes key.
- focused (a list of or a singular dash component, string or number; optional): If true, the input of this label is focused (used by FormGroup components).
- required (boolean; optional): If true, the label will indicate that the input is required.
- className (string; optional): Class name to apply to the component."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, component=Component.UNDEFINED, customStyle=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, error=Component.UNDEFINED, filled=Component.UNDEFINED, focused=Component.UNDEFINED, required=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'component', 'customStyle', 'classes', 'color', 'disabled', 'error', 'filled', 'focused', 'required', 'className']
        self._type = 'FormLabel'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'component', 'customStyle', 'classes', 'color', 'disabled', 'error', 'filled', 'focused', 'required', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FormLabel, self).__init__(children=children, **args)
