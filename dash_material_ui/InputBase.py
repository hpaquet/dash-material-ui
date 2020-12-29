# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class InputBase(Component):
    """An InputBase component.
InputBase component from Material UI

Keyword arguments:
- id (string; optional): The ID of this component.
- classes (dict; optional): Override or extend the styles applied to the component.
- autoComplete (string; optional): This prop helps users to fill forms faster, especially on mobile devices.
- autoFocus (boolean; optional): If true, the input element will be focused during the first mount.
- color (string; optional): The color of the component.
- defaultValue (string; optional): The default input element value. Use when the component is not controlled.
- disabled (boolean; optional): If true, the input element will be disabled.
- error (boolean; optional): If true, the input will indicate an error.
- inputProps (dict; optional): Attributes applied to the input element.
- fullWidth (boolean; optional): If true, the input will take up the full width of its container.
- margin (string; optional): If dense, will adjust vertical spacing.
- multiline (boolean; optional): If true, a textarea element will be rendered.
- name (string; optional): Name attribute of the input element.
- placeholder (string; optional): The short hint displayed in the input before the user enters a value.
- readOnly (boolean; optional): It prevents the user from changing the value of the field (not from interacting with the field).
- rowsMax (number; optional): Maximum number of rows to display when multiline option is set to true.
- rows (number; optional): Number of rows to display when multiline option is set to true.
- rowsMin (number; optional): Minimum number of rows to display when multiline option is set to true.
- type (string; optional): Type of the input element.
- value (string; optional): The value of the input element, required for a controlled component.
- required (boolean; optional): If true, the input element will be required.
- palette (dict; optional): Definition of the palettes.
- style (string; optional): The style of the text field."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, classes=Component.UNDEFINED, autoComplete=Component.UNDEFINED, autoFocus=Component.UNDEFINED, color=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, error=Component.UNDEFINED, inputProps=Component.UNDEFINED, fullWidth=Component.UNDEFINED, margin=Component.UNDEFINED, multiline=Component.UNDEFINED, name=Component.UNDEFINED, placeholder=Component.UNDEFINED, readOnly=Component.UNDEFINED, rowsMax=Component.UNDEFINED, rows=Component.UNDEFINED, rowsMin=Component.UNDEFINED, type=Component.UNDEFINED, value=Component.UNDEFINED, required=Component.UNDEFINED, palette=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'classes', 'autoComplete', 'autoFocus', 'color', 'defaultValue', 'disabled', 'error', 'inputProps', 'fullWidth', 'margin', 'multiline', 'name', 'placeholder', 'readOnly', 'rowsMax', 'rows', 'rowsMin', 'type', 'value', 'required', 'palette', 'style']
        self._type = 'InputBase'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'classes', 'autoComplete', 'autoFocus', 'color', 'defaultValue', 'disabled', 'error', 'inputProps', 'fullWidth', 'margin', 'multiline', 'name', 'placeholder', 'readOnly', 'rowsMax', 'rows', 'rowsMin', 'type', 'value', 'required', 'palette', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(InputBase, self).__init__(**args)
