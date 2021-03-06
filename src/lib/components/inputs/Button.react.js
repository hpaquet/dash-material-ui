import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {omit} from 'ramda';
import MuiButton from '@material-ui/core/Button';
import Icon from '@material-ui/core/Icon';
import { createMuiTheme, withStyles, ThemeProvider } from '@material-ui/core/styles';


/**
 * Button component from Material UI
 */
export default class Button extends Component {

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
            customStyle,
            palette,
            ...otherProps
        } = this.props;

        const theme = createMuiTheme(palette);

        if (this.props.icon) {
            otherProps['startIcon'] = <Icon>{this.props.icon}</Icon>;
        }

        if (customStyle){
            const CustomButton = withStyles(customStyle)(MuiButton);
            return (
                <>
                    <ThemeProvider theme={theme}>
                        <CustomButton onClick={this.handleClick} {...omit(['setProps'], otherProps)}>
                            {this.props.children}
                        </CustomButton>
                    </ThemeProvider>
                </>
            );
        }

        return (
            <>
                <ThemeProvider theme={theme}>
                    <MuiButton onClick={this.handleClick} {...omit(['setProps'], otherProps)}>
                        {this.props.children}
                    </MuiButton>
                </ThemeProvider>
            </>
        );
    }

}

Button.defaultProps = {
    n_clicks: 0,
    n_clicks_timestamp: -1,
    palette: {},
};

Button.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Style to apply to the component container.
     */
    style: PropTypes.object,

    /**
     * Custom button style to apply to the component.
     */
    customStyle: PropTypes.object,

    /**
     * Number of time the component as been clicked on.
     */
    n_clicks: PropTypes.number,

    /**
     * Timestamp of the last time the component as been clicked on.
     */
    n_clicks_timestamp: PropTypes.number,

    /**
     * The content of the component.
     */
    children: PropTypes.node,

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
