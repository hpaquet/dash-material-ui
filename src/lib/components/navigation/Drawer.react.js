import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiDrawer from '@material-ui/core/Drawer';
import {omit} from "ramda";
import {createMuiTheme, ThemeProvider} from "@material-ui/core/styles";


/**
 * Drawer component from Material UI
 */
export default class Drawer extends Component {

    render() {

        const {
            children,
            palette,
            ...otherProps
        } = this.props;

        const theme = createMuiTheme(palette);

        return (
            <ThemeProvider theme={theme}>
                <MuiDrawer {...omit(['setProps'], otherProps)} >
                    {this.props.children}
                </MuiDrawer>
            </ThemeProvider>
        )
    }

}

Drawer.defaultProps = {
};

Drawer.propTypes = {
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
     * Side from which the drawer will appear.
     */
    anchor: PropTypes.string,

    /**
     * The elevation of the drawer.
     */
    elevation: PropTypes.number,

    /**
     * If true, the drawer is open.
     */
    open: PropTypes.bool,

    /**
     * The duration for the transition, in milliseconds.
     */
    transitionDuration: PropTypes.number,

    /**
     * The style of the text field.
     */
    style: PropTypes.string,

    /**
     * The variant to use.
     */
    variant: PropTypes.string,

    /**
     * Definition of the palettes.
     */
    palette: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
