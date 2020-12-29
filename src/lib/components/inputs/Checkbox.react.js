import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiCheckbox from '@material-ui/core/Checkbox';
import {omit} from "ramda";
import {withStyles} from "@material-ui/core/styles";


/**
 * Checkbox component from Material UI
 */
export default class Checkbox extends Component {

    constructor(props) {
        super(props);

        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.props.setProps({checked: event.target.checked});
    }

    render() {

        const {
            customStyle,
            ...otherProps
        } = this.props;

        if (customStyle){
            const CustomCheckbox = withStyles(customStyle)(MuiCheckbox);
            return (
                <>
                    <CustomCheckbox onChange={this.handleChange} {...omit(['setProps'], otherProps)}/>
                </>
            );
        }

        return (
            <>
                <MuiCheckbox onChange={this.handleChange} {...omit(['setProps'], otherProps)}/>
            </>
        );
    }

}

Checkbox.defaultProps = {
    checked: false
};

Checkbox.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Style to apply to the component container.
     */
    style: PropTypes.object,

    /**
     * Custom checkbox style to apply to the component.
     */
    customStyle: PropTypes.object,

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
     * If true, the checkbox will be disabled.
     */
    disabled: PropTypes.bool,

    /**
     * If true, the ripple effect will be disabled.
     */
    disableRipple: PropTypes.bool,

    /**
     * The icon to display when the component is unchecked.
     */
    icon: PropTypes.node,

    /**
     * If true, the component appears indeterminate.
     */
    indeterminate: PropTypes.bool,

    /**
     * The icon to display when the component is indeterminate.
     */
    indeterminateIcon: PropTypes.node,

    /**
     * The size of the checkbox.
     */
    size: PropTypes.string,

    /**
     * The value of the component.
     */
    value: PropTypes.object,

    /**
     * Class name to apply to the component.
     */
    className: PropTypes.string,

};
