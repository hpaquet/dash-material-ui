import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiAppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import {omit} from "ramda";
import {createMuiTheme, ThemeProvider} from "@material-ui/core/styles";


/**
 * AppBar component from Material UI
 */
export default class AppBar extends Component {

    render() {

        const {
            children,
            palette,
            ...otherProps
        } = this.props;

        const theme = createMuiTheme(palette);

        return (
            <ThemeProvider theme={theme}>
                <MuiAppBar {...omit(['setProps'], otherProps)} >
                    <Toolbar>
                        {this.props.children}
                    </Toolbar>
                </MuiAppBar>
            </ThemeProvider>
        )
    }

}

AppBar.defaultProps = {
};

AppBar.propTypes = {
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
     * The color of the component.
     */
    color: PropTypes.string,

    /**
     * Definition of the palettes.
     */
    palette: PropTypes.object,

    /**
     * The positioning type.
     */
    position: PropTypes.string,

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
