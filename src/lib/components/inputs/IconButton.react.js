import React, {Component} from 'react';
import { createMuiTheme, withStyles, ThemeProvider } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import {omit} from 'ramda';
import MuiIconButton from '@material-ui/core/IconButton';
import Badge from '@material-ui/core/Badge';
import Icon from '@material-ui/core/Icon';


/**
 * IconButton component from Material UI
 */
export default class IconButton extends Component {

    constructor(props) {
        super(props);

        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {
        if (!this.props.disabled && this.props.setProps) {
                this.props.setProps({
                    n_clicks: this.props.n_clicks + 1,
                    n_clicks_timestamp: Date.now()
            });
        }
    }

    render() {
        const {
            ariaLabel,
            badgeContent,
            badgeMaxContent,
            badgeAnchorOrigin,
            badgeOverlap,
            badgeVariant,
            badgeInvisible,
            badgeShowZero,
            badgeColor,
            customStyle,
            palette,
            ...otherProps
        } = this.props;

        const theme = createMuiTheme(palette);

        if (customStyle){
            const CustomButton = withStyles(customStyle)(MuiIconButton);
            return (
                <>
                    <ThemeProvider theme={theme}>
                        <CustomButton aria-label={ariaLabel} onClick={this.handleClick} {...omit(['setProps'], otherProps)}>
                            <Badge
                                badgeContent={badgeContent}
                                max={badgeMaxContent}
                                anchorOrigin={badgeAnchorOrigin}
                                color={badgeColor}
                                overlap={badgeOverlap}
                                variant={badgeVariant}
                                invisible={badgeInvisible}
                                showZero={badgeShowZero}>
                                <Icon>{this.props.icon}</Icon>
                            </Badge>
                        </CustomButton>
                    </ThemeProvider>
                </>
            );
        }

        return (
            <>
                <ThemeProvider theme={theme}>
                    <MuiIconButton aria-label={ariaLabel} onClick={this.handleClick} {...omit(['setProps'], otherProps)}>
                            <Badge
                                badgeContent={badgeContent}
                                max={badgeMaxContent}
                                anchorOrigin={badgeAnchorOrigin}
                                color={badgeColor}
                                overlap={badgeOverlap}
                                variant={badgeVariant}
                                invisible={badgeInvisible}
                                showZero={badgeShowZero}>
                            <Icon>{this.props.icon}</Icon>
                        </Badge>
                    </MuiIconButton>
                </ThemeProvider>
            </>
        );
    }

}

IconButton.defaultProps = {
    n_clicks: 0,
    n_clicks_timestamp: -1,
    palette: {},
    badgeContent: 0,
};

IconButton.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Style to apply to the component container.
     */
    style: PropTypes.object,

    /**
     * 	The content rendered within the badge.
     */
    badgeContent: PropTypes.number,

    /**
     * Max count to show in badge.
     */
    badgeMaxContent: PropTypes.number,

    /**
     * The anchor of the badge.
     */
    badgeAnchorOrigin: PropTypes.string,

    /**
     * Wrapped shape the badge should overlap.
     */
    badgeOverlap: PropTypes.string,

    /**
     * The variant to use in the badge.
     */
    badgeVariant: PropTypes.string,

    /**
     * 	If true, the badge will be invisible.
     */
    badgeInvisible: PropTypes.bool,

    /**
     * The color of the badge.
     */
    badgeColor: PropTypes.string,

    /**
     * Controls whether the badge is hidden when badgeContent is zero.
     */
    badgeShowZero: PropTypes.bool,

    /**
     * If given, uses a negative margin to counteract the padding on one side.
     */
    edge: PropTypes.string,

    /**
     * Custom button style to apply to the component.
     */
    customStyle: PropTypes.object,

    /**
     * Style to apply to the component container.
     */
    ariaLabel: PropTypes.string,

    /**
     * Number of time the component as been clicked on.
     */
    n_clicks: PropTypes.number,

    /**
     * Timestamp of the last time the component as been clicked on.
     */
    n_clicks_timestamp: PropTypes.number,

    /**
     * Override or extend the styles applied to the component.
     */
    classes: PropTypes.object,

    /**
     * The color of the component.
     */
    color: PropTypes.string,

    /**
     * If true, the button will be disabled.
     */
    disabled: PropTypes.bool,

    /**
     * If true, no elevation is used.
     */
    disableElevation: PropTypes.bool,

    /**
     * If true, the keyboard focus ripple will be disabled.
     */
    disableFocusRipple: PropTypes.bool,

    /**
     * If true, the ripple effect will be disabled.
     */
    disableRipple: PropTypes.bool,

    /**
     * Name of the icon.
     */
    icon: PropTypes.string,

    /**
     * If true, the button will take up the full width of its container.
     */
    fullWidth: PropTypes.node,

    /**
     * The URL to link to when the button is clicked.
     */
    href: PropTypes.string,

    /**
     * The size of the button.
     */
    size: PropTypes.string,

    /**
     * Position of the icon (start/end).
     */
    iconPosition: PropTypes.string,

    /**
     * Definition of the palettes.
     */
    palette: PropTypes.object,

    /**
     * The variant to use.
     */
    variant: PropTypes.string,

    /**
     * Class name to apply to the component.
     */
    className: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
