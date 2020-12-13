import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {omit} from 'ramda';
import MuiButton from '@material-ui/core/Button';


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
                    n_clicks: n_clicks + 1,
                    n_clicks_timestamp: Date.now()
            });
        }
    }

    render() {
        const {
            id,
            ...otherProps
        } = props;

        return (
            <>
                <MuiButton id={id} onClick={this.handleClick}  {...omit(['setProps'], otherProps)}>
                    {props.children}
                </MuiButton>
            </>
        );
    }

}

Button.defaultProps = {
    n_clicks: 0,
    n_clicks_timestamp: -1,
};

Button.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string.isRequired,

    /**
     * Style to apply to the component container.
     */
    style: PropTypes.object,

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
     * Element placed after the children.
     */
    endIcon: PropTypes.node,

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
     * Element placed before the children.
     */
    startIcon: PropTypes.object,

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
