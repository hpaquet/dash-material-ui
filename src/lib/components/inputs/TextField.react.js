import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiTextField from '@material-ui/core/TextField';
import {omit} from "ramda";

/**
 * Text field component from Material UI
 */
export default class TextField extends Component {

    render() {

        const {
            id,
            ...otherProps
        } = this.props;

        return (
                <MuiTextField id={id} {...omit(['setProps'], otherProps)}/>
            )
    }

}

TextField.defaultProps = {
};

TextField.propTypes = {
    /**
     * The ID of this component.
     */
    id: PropTypes.string,

    /**
     * This prop helps users to fill forms faster, especially on mobile devices.
     */
    autoComplete: PropTypes.bool,

    /**
     * 	If true, the input element will be focused during the first mount.
     */
    autoFocus: PropTypes.node,

    /**
     * Override or extend the styles applied to the component.
     */
    classes: PropTypes.object,

    /**
     * The color of the component.
     */
    color: PropTypes.string,

    /**
     * The default value of the input element.
     */
    defaultValue: PropTypes.string,

    /**
     * If true, the input element will be disabled.
     */
    disabled: PropTypes.bool,

    /**
     * 	If true, the label will be displayed in an error state.
     */
    error: PropTypes.bool,

    /**
     * Props applied to the FormHelperText element.
     */
    FormHelperTextProps: PropTypes.object,

    /**
     * If true, the input will take up the full width of its container.
     */
    fullWidth: PropTypes.bool,

    /**
     * Props applied to the InputLabel element.
     */
    InputLabelProps: PropTypes.object,

    /**
     * 	Attributes applied to the input element.
     */
    inputProps: PropTypes.object,

    /**
     * 	The label content.
     */
    label: PropTypes.string,

    /**
     * If dense or normal, will adjust vertical spacing of this and contained components.
     */
    margin: PropTypes.string,

    /**
     * If true, a textarea element will be rendered instead of an input.
     */
    multiline: PropTypes.bool,

    /**
     * 	Name attribute of the input element.
     */
    name: PropTypes.string,

    /**
     * 	The short hint displayed in the input before the user enters a value.
     */
    placeholder: PropTypes.string,

    /**
     * 	Number of rows to display when multiline option is set to true.
     */
    rows: PropTypes.number,

    /**
     * 	Maximum number of rows to display when multiline option is set to true.
     */
    rowsMax: PropTypes.number,

    /**
     * 	Maximum number of rows to display when multiline option is set to true.
     */
    select: PropTypes.bool,

    /**
     * The size of the text field.
     */
    size: PropTypes.string,

    /**
     * 	Type of the input element. It should be a valid HTML5 input type.
     */
    type: PropTypes.string,

    /**
     * The style of the text field.
     */
    style: PropTypes.string,

    /**
     * The value of the input element, required for a controlled component.
     */
    value: PropTypes.string,

    /**
     * The variant to use.
     */
    variant: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
