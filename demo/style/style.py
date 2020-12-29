from css_generator import StyleSheet
from css_generator import Rule
from css_generator import Media

from demo.style import theme

stylesheet = StyleSheet()

root = Rule(
    rule_selector='bar-root',
    rule_type='class',
    properties={
        'flex-grow': 1,
    }
)

menu_button = Rule(
    rule_selector='bar-menu-button',
    rule_type='class',
    properties={
        'margin-right': theme.spacing(2),
    }
)

title = Rule(
    rule_selector='bar-title',
    rule_type='class',
    properties=[
        {
            'display': 'none',
            'flex-grow': 1,
        },
        Media(
            rule_selector=theme.breakpoints.up('sm'),
            properties={
                'display': 'block',
            }
        ),
    ]
)

search = Rule(
    rule_selector='bar-search',
    rule_type='class',
    properties=[
        {
            'position': 'relative',
            'border-radius': theme.shape.border_radius,
            # 'background-color': theme.palette.common.white,
            'margin-right': theme.spacing(2),
            'margin-left': 0,
            'width': '100%',
            'display': 'block',
        },
        Media(
            rule_selector=theme.breakpoints.up('sm'),
            properties={
                'margin-left': theme.spacing(1),
                'width': 'auto',
            }
        ),
        # Rule(
        #     rule_selector='&',
        #     pseudo_class='hover',
        #     properties={
        #         'background-color': theme.palette.common.white,
        #     }
        # ),
    ]
)

search_icon = Rule(
    rule_selector='bar-search-icon',
    rule_type='class',
    properties={
                'padding': theme.spacing(0, 2),
                'height': '100%',
                'position': 'absolute',
                'pointer-events': 'none',
                'display': 'flex',
                'align-items': 'center',
                'justify-content': 'center',
        }
)

input_root = Rule(
    rule_selector='bar-input-root',
    rule_type='class',
    properties={
        'color': 'inherit',
    }
)

input_input = Rule(
    rule_selector='bar-input-input',
    rule_type='class',
    properties=[{
            'padding': theme.spacing(1, 1, 1, 0),
            'padding-left': f'calc(1em + {theme.spacing(4)}) !important',
            # 'transition': theme.transitions.create('width'),
            'width': '100%',
            },
            Media(
                rule_selector=theme.breakpoints.up('md'),
                properties={
                    'width': '20ch',
                }
            ),
    ]
)

section_desktop = Rule(
    rule_selector='bar-section-desktop',
    rule_type='class',
    properties=[{
            'display': 'none',
            },
            Media(
                rule_selector=theme.breakpoints.up('md'),
                properties={
                    'display': 'flex',
                }
            ),
    ]
)

section_mobile = Rule(
    rule_selector='bar-section-mobile',
    rule_type='class',
    properties=[{
            'display': 'flex',
            },
            Media(
                rule_selector=theme.breakpoints.up('md'),
                properties={
                    'display': 'none',
                }
            ),
    ]
)

stylesheet.add_rules([
    root,
    menu_button,
    title,
    search,
    search_icon,
    input_root,
    input_input,
    section_desktop,
    section_mobile,
])