# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Box(Component):
    """A Box component.
Box component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the link.
- id (string; optional): The ID of this component.
- className (dict; optional): Override or extend the styles applied to the component.
- disableGutters (boolean; optional): If true, the left and right padding is removed.
- fixed (boolean; optional): Set the max-width to match the min-width of the current breakpoint.
- maxWidth (boolean; optional): Determine the max-width of the container.
- style (string; optional): The style of the text field."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, disableGutters=Component.UNDEFINED, fixed=Component.UNDEFINED, maxWidth=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'disableGutters', 'fixed', 'maxWidth', 'style']
        self._type = 'Box'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'disableGutters', 'fixed', 'maxWidth', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Box, self).__init__(children=children, **args)
