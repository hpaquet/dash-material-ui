import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MUISwitch from '@material-ui/core/Switch';
import {omit} from "ramda";

/**
 * Switch component from Material UI
 */
export default class Switch extends Component {

    constructor(props) {
        super(props);

        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.props.setProps({checked: event.target.checked});
    }

    render() {

        const {
            id,
            ...otherProps
        } = this.props;

        return (
                <MUISwitch id={id} checked={this.props.checked} onChange={this.handleChange} {...omit(['setProps'], otherProps)}/>
            )
    }

}

Switch.defaultProps = {
    checked: false
};

Switch.propTypes = {
    /**
     * The ID of this component.
     */
    id: PropTypes.string,

    /**
     * If true, the component is checked.
     */
    checked: PropTypes.bool,

    /**
     * The icon to display when the component is checked.
     */
    checkedIcon: PropTypes.node,

    /**
     * Override or extend the styles applied to the component.
     */
    classes: PropTypes.object,

    /**
     * The color of the component.
     */
    color: PropTypes.string,

    /**
     * If true, the switch will be disabled.
     */
    disabled: PropTypes.bool,

    /**
     * If true, the ripple effect will be disabled.
     */
    disableRipple: PropTypes.bool,

    /**
     * If given, uses a negative margin to counteract the padding on one side.
     */
    edge: PropTypes.string,

    /**
     * The icon to display when the component is unchecked.
     */
    icon: PropTypes.node,

    /**
     * The size of the switch.
     */
    size: PropTypes.string,

    /**
     * The style of the switch.
     */
    style: PropTypes.string,

    /**
     * The value of the component.
     */
    value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
