# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class IconButton(Component):
    """An IconButton component.
IconButton component from Material UI

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- style (dict; optional): Style to apply to the component container.
- badgeContent (number; default 0): The content rendered within the badge.
- badgeMaxContent (number; optional): Max count to show in badge.
- badgeAnchorOrigin (string; optional): The anchor of the badge.
- badgeOverlap (string; optional): Wrapped shape the badge should overlap.
- badgeVariant (string; optional): The variant to use in the badge.
- badgeInvisible (boolean; optional): If true, the badge will be invisible.
- badgeColor (string; optional): The color of the badge.
- badgeShowZero (boolean; optional): Controls whether the badge is hidden when badgeContent is zero.
- edge (string; optional): If given, uses a negative margin to counteract the padding on one side.
- customStyle (dict; optional): Custom button style to apply to the component.
- ariaLabel (string; optional): Style to apply to the component container.
- n_clicks (number; default 0): Number of time the component as been clicked on.
- n_clicks_timestamp (number; default -1): Timestamp of the last time the component as been clicked on.
- classes (dict; optional): Override or extend the styles applied to the component.
- color (string; optional): The color of the component.
- disabled (boolean; optional): If true, the button will be disabled.
- disableElevation (boolean; optional): If true, no elevation is used.
- disableFocusRipple (boolean; optional): If true, the keyboard focus ripple will be disabled.
- disableRipple (boolean; optional): If true, the ripple effect will be disabled.
- icon (string; optional): Name of the icon.
- fullWidth (a list of or a singular dash component, string or number; optional): If true, the button will take up the full width of its container.
- href (string; optional): The URL to link to when the button is clicked.
- size (string; optional): The size of the button.
- iconPosition (string; optional): Position of the icon (start/end).
- palette (dict; optional): Definition of the palettes.
- variant (string; optional): The variant to use.
- className (string; optional): Class name to apply to the component."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, badgeContent=Component.UNDEFINED, badgeMaxContent=Component.UNDEFINED, badgeAnchorOrigin=Component.UNDEFINED, badgeOverlap=Component.UNDEFINED, badgeVariant=Component.UNDEFINED, badgeInvisible=Component.UNDEFINED, badgeColor=Component.UNDEFINED, badgeShowZero=Component.UNDEFINED, edge=Component.UNDEFINED, customStyle=Component.UNDEFINED, ariaLabel=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, disableElevation=Component.UNDEFINED, disableFocusRipple=Component.UNDEFINED, disableRipple=Component.UNDEFINED, icon=Component.UNDEFINED, fullWidth=Component.UNDEFINED, href=Component.UNDEFINED, size=Component.UNDEFINED, iconPosition=Component.UNDEFINED, palette=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'style', 'badgeContent', 'badgeMaxContent', 'badgeAnchorOrigin', 'badgeOverlap', 'badgeVariant', 'badgeInvisible', 'badgeColor', 'badgeShowZero', 'edge', 'customStyle', 'ariaLabel', 'n_clicks', 'n_clicks_timestamp', 'classes', 'color', 'disabled', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'icon', 'fullWidth', 'href', 'size', 'iconPosition', 'palette', 'variant', 'className']
        self._type = 'IconButton'
        self._namespace = 'dash_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'style', 'badgeContent', 'badgeMaxContent', 'badgeAnchorOrigin', 'badgeOverlap', 'badgeVariant', 'badgeInvisible', 'badgeColor', 'badgeShowZero', 'edge', 'customStyle', 'ariaLabel', 'n_clicks', 'n_clicks_timestamp', 'classes', 'color', 'disabled', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'icon', 'fullWidth', 'href', 'size', 'iconPosition', 'palette', 'variant', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(IconButton, self).__init__(**args)
