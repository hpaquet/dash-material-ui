# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TextField(Component):
    """A TextField component.
Text field component from Material UI

Keyword arguments:
- id (string; optional): The ID of this component.
- autoComplete (boolean; optional): This prop helps users to fill forms faster, especially on mobile devices.
- autoFocus (a list of or a singular dash component, string or number; optional): If true, the input element will be focused during the first mount.
- classes (dict; optional): Override or extend the styles applied to the component.
- color (string; optional): The color of the component.
- defaultValue (string; optional): The default value of the input element.
- disabled (boolean; optional): If true, the input element will be disabled.
- error (boolean; optional): If true, the label will be displayed in an error state.
- FormHelperTextProps (dict; optional): Props applied to the FormHelperText element.
- fullWidth (boolean; optional): If true, the input will take up the full width of its container.
- InputLabelProps (dict; optional): Props applied to the InputLabel element.
- inputProps (dict; optional): Attributes applied to the input element.
- label (string; optional): The label content.
- margin (string; optional): If dense or normal, will adjust vertical spacing of this and contained components.
- multiline (boolean; optional): If true, a textarea element will be rendered instead of an input.
- name (string; optional): Name attribute of the input element.
- placeholder (string; optional): The short hint displayed in the input before the user enters a value.
- rows (number; optional): Number of rows to display when multiline option is set to true.
- rowsMax (number; optional): Maximum number of rows to display when multiline option is set to true.
- select (boolean; optional): Maximum number of rows to display when multiline option is set to true.
- size (string; optional): The size of the text field.
- type (string; optional): Type of the input element. It should be a valid HTML5 input type.
- style (string; optional): The style of the text field.
- value (string; optional): The value of the input element, required for a controlled component.
- variant (string; optional): The variant to use."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, autoComplete=Component.UNDEFINED, autoFocus=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, error=Component.UNDEFINED, FormHelperTextProps=Component.UNDEFINED, fullWidth=Component.UNDEFINED, InputLabelProps=Component.UNDEFINED, inputProps=Component.UNDEFINED, label=Component.UNDEFINED, margin=Component.UNDEFINED, multiline=Component.UNDEFINED, name=Component.UNDEFINED, placeholder=Component.UNDEFINED, rows=Component.UNDEFINED, rowsMax=Component.UNDEFINED, select=Component.UNDEFINED, size=Component.UNDEFINED, type=Component.UNDEFINED, style=Component.UNDEFINED, value=Component.UNDEFINED, variant=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoComplete', 'autoFocus', 'classes', 'color', 'defaultValue', 'disabled', 'error', 'FormHelperTextProps', 'fullWidth', 'InputLabelProps', 'inputProps', 'label', 'margin', 'multiline', 'name', 'placeholder', 'rows', 'rowsMax', 'select', 'size', 'type', 'style', 'value', 'variant']
        self._type = 'TextField'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoComplete', 'autoFocus', 'classes', 'color', 'defaultValue', 'disabled', 'error', 'FormHelperTextProps', 'fullWidth', 'InputLabelProps', 'inputProps', 'label', 'margin', 'multiline', 'name', 'placeholder', 'rows', 'rowsMax', 'select', 'size', 'type', 'style', 'value', 'variant']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(TextField, self).__init__(**args)
