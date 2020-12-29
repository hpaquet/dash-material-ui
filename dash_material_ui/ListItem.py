# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ListItem(Component):
    """A ListItem component.
ListItem component from Material UI

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The content of the list.
- id (string; optional): The ID of this component.
- classes (dict; optional): Override or extend the styles applied to the component.
- className (string; optional): Often used with CSS to style elements with common properties.
- alignItems (string; optional): Defines the align-items style property.
- autoFocus (string; optional): If true, the list item will be focused during the first mount.
- button (boolean; optional): If true, the list item will be a button (using ButtonBase).
- dense (boolean; optional): If true, compact vertical padding designed for keyboard and mouse input will be used.
- disabled (boolean; optional): If true, the list item will be disabled.
- disableGutters (boolean; optional): If true, the left and right padding is removed.
- divider (boolean; optional): If true, a 1px light border is added to the bottom of the list item.
- selected (boolean; optional): Use to apply selected styling.
- primary (string; optional): The main content element.
- secondary (string; optional): The secondary content element.
- icon (string; optional): Icon of the item
- avatarIcon (string; optional): Avatar icon of the item
- inset (boolean; optional): If true, the children will be indented.
- palette (dict; optional): Definition of the palettes."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, classes=Component.UNDEFINED, className=Component.UNDEFINED, alignItems=Component.UNDEFINED, autoFocus=Component.UNDEFINED, button=Component.UNDEFINED, dense=Component.UNDEFINED, disabled=Component.UNDEFINED, disableGutters=Component.UNDEFINED, divider=Component.UNDEFINED, selected=Component.UNDEFINED, primary=Component.UNDEFINED, secondary=Component.UNDEFINED, icon=Component.UNDEFINED, avatarIcon=Component.UNDEFINED, inset=Component.UNDEFINED, palette=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'classes', 'className', 'alignItems', 'autoFocus', 'button', 'dense', 'disabled', 'disableGutters', 'divider', 'selected', 'primary', 'secondary', 'icon', 'avatarIcon', 'inset', 'palette']
        self._type = 'ListItem'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'classes', 'className', 'alignItems', 'autoFocus', 'button', 'dense', 'disabled', 'disableGutters', 'divider', 'selected', 'primary', 'secondary', 'icon', 'avatarIcon', 'inset', 'palette']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ListItem, self).__init__(children=children, **args)
