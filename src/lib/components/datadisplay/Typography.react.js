import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiTypography from '@material-ui/core/Typography';
import {omit} from "ramda";
import {createMuiTheme, ThemeProvider, createStyles} from "@material-ui/core/styles";

/**
 * Typography component from Material UI
 */
export default class Typography extends Component {

    render() {

        const {
            children,
            palette,
            ...otherProps
        } = this.props;

        const theme = createMuiTheme(palette);

        return (
            <ThemeProvider theme={theme}>
                <MuiTypography {...omit(['setProps'], otherProps)} >
                    {this.props.children}
                </MuiTypography>
            </ThemeProvider>
        )
    }

}

Typography.defaultProps = {
};

Typography.propTypes = {
    /**
     * The ID of this component.
     */
    id: PropTypes.string,

    /**
     * The content of the drawer.
     */
    children: PropTypes.node,

    /**
     * Override or extend the styles applied to the component.
     */
    classes: PropTypes.object,

    /**
     * Often used with CSS to style elements with common properties.
     */
    className: PropTypes.string,

    /**
     * Set the text-align on the component.
     */
    align: PropTypes.string,

    /**
     * The color of the component.
     */
    color: PropTypes.string,

    /**
     * Controls the display type
     */
    display: PropTypes.string,

    /**
     * 	If true, the text will have a bottom margin.
     */
    gutterBottom: PropTypes.bool,

    /**
     * 	If true, the text will not wrap, but instead will truncate with a text overflow ellipsis.
     */
    noWrap: PropTypes.bool,

    /**
     * 	If true, the text will have a bottom margin.
     */
    paragraph: PropTypes.string,

    /**
     * Definition of the palettes.
     */
    palette: PropTypes.object,

    /**
     * The style of the text field.
     */
    style: PropTypes.string,

    /**
     * Applies the style typography styles.
     */
    variant: PropTypes.string,

    /**
     * The component maps the variant prop to a range of different HTML element types.
     */
    variantMapping: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
