import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiInputBase from '@material-ui/core/InputBase';
import {omit} from "ramda";
import {createMuiTheme, ThemeProvider} from "@material-ui/core/styles";


/**
 * InputBase component from Material UI
 */
export default class InputBase extends Component {

    render() {

        const {
            palette,
            ...otherProps
        } = this.props;

        const theme = createMuiTheme(palette);

        return (
            <ThemeProvider theme={theme}>
                <MuiInputBase {...omit(['setProps'], otherProps)} />
            </ThemeProvider>
        )
    }

}

InputBase.defaultProps = {
};

InputBase.propTypes = {
    /**
     * The ID of this component.
     */
    id: PropTypes.string,

    /**
     * Override or extend the styles applied to the component.
     */
    classes: PropTypes.object,

    /**
     * This prop helps users to fill forms faster, especially on mobile devices.
     */
    autoComplete: PropTypes.string,

    /**
     * If true, the input element will be focused during the first mount.
     */
    autoFocus: PropTypes.bool,

    /**
     * The color of the component.
     */
    color: PropTypes.string,

    /**
     * The default input element value. Use when the component is not controlled.
     */
    defaultValue: PropTypes.string,

    /**
     * If true, the input element will be disabled.
     */
    disabled: PropTypes.bool,

    /**
     * If true, the input will indicate an error.
     */
    error: PropTypes.bool,

    /**
     * Attributes applied to the input element.
     */
    inputProps: PropTypes.object,

    /**
     * If true, the input will take up the full width of its container.
     */
    fullWidth: PropTypes.bool,

    /**
     * If dense, will adjust vertical spacing.
     */
    margin: PropTypes.string,

    /**
     * If true, a textarea element will be rendered.
     */
    multiline: PropTypes.bool,

    /**
     * 	Name attribute of the input element.
     */
    name: PropTypes.string,

    /**
     *  The short hint displayed in the input before the user enters a value.
     */
    placeholder: PropTypes.string,

    /**
     *  It prevents the user from changing the value of the field (not from interacting with the field).
     */
    readOnly: PropTypes.bool,

    /**
     *  Maximum number of rows to display when multiline option is set to true.
     */
    rowsMax: PropTypes.number,

    /**
     *  Number of rows to display when multiline option is set to true.
     */
    rows: PropTypes.number,

    /**
     *  Minimum number of rows to display when multiline option is set to true.
     */
    rowsMin: PropTypes.number,

    /**
     *  Type of the input element.
     */
    type: PropTypes.string,

    /**
     *  The value of the input element, required for a controlled component.
     */
    value: PropTypes.string,

    /**
     *  If true, the input element will be required.
     */
    required: PropTypes.bool,

    /**
     * Definition of the palettes.
     */
    palette: PropTypes.object,

    /**
     * The style of the text field.
     */
    style: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
