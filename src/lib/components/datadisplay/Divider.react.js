import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiDivider from '@material-ui/core/Divider';
import {omit} from "ramda";
import {createMuiTheme, ThemeProvider} from "@material-ui/core/styles";

/**
 * Divider component from Material UI
 */
export default class Divider extends Component {

    render() {

        const {
            palette,
            ...otherProps
        } = this.props;

        const theme = createMuiTheme(palette);

        return (
            <ThemeProvider theme={theme}>
                <MuiDivider {...omit(['setProps'], otherProps)} />
            </ThemeProvider>
        )
    }

}

Divider.defaultProps = {
};

Divider.propTypes = {
    /**
     * The ID of this component.
     */
    id: PropTypes.string,

    /**
     * Override or extend the styles applied to the component.
     */
    classes: PropTypes.object,

    /**
     * Often used with CSS to style elements with common properties.
     */
    className: PropTypes.string,

    /**
     * 	Absolutely position the element.
     */
    absolute: PropTypes.bool,

    /**
     * If true, a vertical divider will have the correct height when used in flex container.
     */
    flexItem: PropTypes.bool,

    /**
     * If true, the divider will have a lighter color.
     */
    light: PropTypes.bool,

    /**
     * 	The divider orientation.
     */
    orientation: PropTypes.string,

    /**
     * 	The variant to use.
     */
    variant: PropTypes.string,

    /**
     * Definition of the palettes.
     */
    palette: PropTypes.object,

    /**
     * The style of the divider.
     */
    style: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
