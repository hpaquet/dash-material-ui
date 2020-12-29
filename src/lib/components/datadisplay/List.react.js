import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiList from '@material-ui/core/List';
import {omit} from "ramda";
import {createMuiTheme, ThemeProvider} from "@material-ui/core/styles";

/**
 * List component from Material UI
 */
export default class List extends Component {

    render() {

        const {
            ariaLabel,
            children,
            palette,
            ...otherProps
        } = this.props;

        const theme = createMuiTheme(palette);

        return (
            <ThemeProvider theme={theme}>
                <MuiList aria-label={ariaLabel} {...omit(['setProps'], otherProps)} >
                    {this.props.children}
                </MuiList>
            </ThemeProvider>
        )
    }

}

List.defaultProps = {
};

List.propTypes = {
    /**
     * The ID of this component.
     */
    id: PropTypes.string,

    /**
     * Aria-Label of the list.
     */
    ariaLabel: PropTypes.node,

    /**
     * The content of the list.
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
     * If true, compact vertical padding designed for keyboard and mouse input will be used for the list and list items.
     */
    dense: PropTypes.bool,

    /**
     * 	If true, vertical padding will be removed from the list.
     */
    disablePadding: PropTypes.bool,

    /**
     * 	The content of the subheader, normally ListSubheader.
     */
    subheader: PropTypes.node,

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
