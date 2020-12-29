import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiIcon from '@material-ui/core/Icon';
import {omit} from "ramda";
import {createMuiTheme, ThemeProvider} from "@material-ui/core/styles";


/**
 * Icon component from Material UI
 */
export default class Icon extends Component {

    render() {

        const {
            children,
            palette,
            ...otherProps
        } = this.props;

        const theme = createMuiTheme(palette);

        return (
            <ThemeProvider theme={theme}>
                <MuiIcon {...omit(['setProps'], otherProps)} >
                    {this.props.children}
                </MuiIcon>
            </ThemeProvider>
        )
    }

}

Icon.defaultProps = {
};

Icon.propTypes = {
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
     * The color of the component.
     */
    color: PropTypes.string,

    /**
     * The fontSize applied to the icon.
     */
    fontSize: PropTypes.string,

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
