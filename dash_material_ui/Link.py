# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Link(Component):
    """A Link component.
Link component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the link.
- id (string; optional): The ID of this component.
- classes (dict; optional): Override or extend the styles applied to the component.
- color (string; optional): The color of the component.
- TypographyClasses (dict; optional): Classes prop applied to the Typography element.
- underline (string; optional): Controls when the link should have an underline.
- style (string; optional): The style of the text field.
- variant (string; optional): The variant to use."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, TypographyClasses=Component.UNDEFINED, underline=Component.UNDEFINED, style=Component.UNDEFINED, variant=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'classes', 'color', 'TypographyClasses', 'underline', 'style', 'variant']
        self._type = 'Link'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'classes', 'color', 'TypographyClasses', 'underline', 'style', 'variant']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Link, self).__init__(children=children, **args)
