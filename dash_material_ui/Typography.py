# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Typography(Component):
    """A Typography component.
Typography component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the drawer.
- id (string; optional): The ID of this component.
- classes (dict; optional): Override or extend the styles applied to the component.
- className (string; optional): Often used with CSS to style elements with common properties.
- align (string; optional): Set the text-align on the component.
- color (string; optional): The color of the component.
- display (string; optional): Controls the display type
- gutterBottom (boolean; optional): If true, the text will have a bottom margin.
- noWrap (boolean; optional): If true, the text will not wrap, but instead will truncate with a text overflow ellipsis.
- paragraph (string; optional): If true, the text will have a bottom margin.
- palette (dict; optional): Definition of the palettes.
- style (string; optional): The style of the text field.
- variant (string; optional): Applies the style typography styles.
- variantMapping (dict; optional): The component maps the variant prop to a range of different HTML element types."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, classes=Component.UNDEFINED, className=Component.UNDEFINED, align=Component.UNDEFINED, color=Component.UNDEFINED, display=Component.UNDEFINED, gutterBottom=Component.UNDEFINED, noWrap=Component.UNDEFINED, paragraph=Component.UNDEFINED, palette=Component.UNDEFINED, style=Component.UNDEFINED, variant=Component.UNDEFINED, variantMapping=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'classes', 'className', 'align', 'color', 'display', 'gutterBottom', 'noWrap', 'paragraph', 'palette', 'style', 'variant', 'variantMapping']
        self._type = 'Typography'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'classes', 'className', 'align', 'color', 'display', 'gutterBottom', 'noWrap', 'paragraph', 'palette', 'style', 'variant', 'variantMapping']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Typography, self).__init__(children=children, **args)
