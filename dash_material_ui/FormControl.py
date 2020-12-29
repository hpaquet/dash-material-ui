# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FormControl(Component):
    """A FormControl component.
FormControl component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the component.
- id (string; optional): The ID used to identify this component in Dash callbacks.
- style (dict; optional): Style to apply to the component container.
- customStyle (dict; optional): Custom FormControl style to apply to the component.
- classes (dict; optional): Override or extend the styles applied to the component.
- color (string; optional): The color of the component.
- component (string; optional): The component used for the root node.
- disabled (boolean; optional): If true, the FormControl will be disabled.
- error (boolean; optional): If true, the label should be displayed in an error state.
- focused (boolean; optional): If true, the component will be displayed in focused state.
- fullWidth (a list of or a singular dash component, string or number; optional): If true, the FormControl will take up the full width of its container.
- hiddenLabel (boolean; optional): If true, the label will be hidden.
- margin (string; optional): If dense or normal, will adjust vertical spacing of this and contained components.
- required (string; optional): If true, the label will indicate that the input is required.
- size (string; optional): The size of the FormControl.
- variant (string; optional): The variant to use.
- className (string; optional): Class name to apply to the component."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, customStyle=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, component=Component.UNDEFINED, disabled=Component.UNDEFINED, error=Component.UNDEFINED, focused=Component.UNDEFINED, fullWidth=Component.UNDEFINED, hiddenLabel=Component.UNDEFINED, margin=Component.UNDEFINED, required=Component.UNDEFINED, size=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'customStyle', 'classes', 'color', 'component', 'disabled', 'error', 'focused', 'fullWidth', 'hiddenLabel', 'margin', 'required', 'size', 'variant', 'className']
        self._type = 'FormControl'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'customStyle', 'classes', 'color', 'component', 'disabled', 'error', 'focused', 'fullWidth', 'hiddenLabel', 'margin', 'required', 'size', 'variant', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FormControl, self).__init__(children=children, **args)
