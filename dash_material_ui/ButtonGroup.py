# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ButtonGroup(Component):
    """A ButtonGroup component.
Button group component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the component.
- id (string; required): The ID used to identify this component in Dash callbacks.
- style (dict; optional): Style to apply to the component container.
- classes (dict; optional): Override or extend the styles applied to the component.
- color (string; optional): The color of the component.
- disabled (boolean; optional): If true, the button will be disabled.
- disableElevation (boolean; optional): If true, no elevation is used.
- disableFocusRipple (boolean; optional): If true, the keyboard focus ripple will be disabled.
- disableRipple (boolean; optional): If true, the ripple effect will be disabled.
- fullWidth (a list of or a singular dash component, string or number; optional): If true, the button will take up the full width of its container.
- orientation (a list of or a singular dash component, string or number; optional): If true, the button will take up the full width of its container.
- size (string; optional): The size of the button.
- variant (string; optional): The variant to use.
- className (string; default ''): Class name to apply to the component.
- ariaLabel (string; optional): Aria label to apply to the component."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.REQUIRED, style=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, disableElevation=Component.UNDEFINED, disableFocusRipple=Component.UNDEFINED, disableRipple=Component.UNDEFINED, fullWidth=Component.UNDEFINED, orientation=Component.UNDEFINED, size=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, ariaLabel=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'classes', 'color', 'disabled', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'fullWidth', 'orientation', 'size', 'variant', 'className', 'ariaLabel']
        self._type = 'ButtonGroup'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'classes', 'color', 'disabled', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'fullWidth', 'orientation', 'size', 'variant', 'className', 'ariaLabel']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ButtonGroup, self).__init__(children=children, **args)
