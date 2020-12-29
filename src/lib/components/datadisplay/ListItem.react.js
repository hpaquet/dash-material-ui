import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import {omit} from "ramda";
import {createMuiTheme, ThemeProvider} from "@material-ui/core/styles";
import Icon from "@material-ui/core/Icon";

/**
 * ListItem component from Material UI
 */
export default class ListItem extends Component {

    render() {

        const {
            children,
            palette,
            primary,
            secondary,
            inset,
            ...otherProps
        } = this.props;

        const theme = createMuiTheme(palette);

        return (
            <ThemeProvider theme={theme}>
                <MuiListItem {...omit(['setProps'], otherProps)} >
                    {this.props.icon && <ListItemIcon><Icon>{this.props.icon}</Icon></ListItemIcon>}
                    {this.props.avatarIcon && <ListItemIcon><avatar><Icon>{this.props.avatarIcon}</Icon></avatar></ListItemIcon>}
                    <ListItemText primary={primary} secondary={secondary} inset={inset}/>
                </MuiListItem>
            </ThemeProvider>
        )
    }
}

ListItem.defaultProps = {
};

ListItem.propTypes = {
    /**
     * The ID of this component.
     */
    id: PropTypes.string,

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
     * Defines the align-items style property.
     */
    alignItems: PropTypes.string,

    /**
     * If true, the list item will be focused during the first mount.
     */
    autoFocus: PropTypes.string,

    /**
     * If true, the list item will be a button (using ButtonBase).
     */
    button: PropTypes.bool,

    /**
     * If true, compact vertical padding designed for keyboard and mouse input will be used.
     */
    dense: PropTypes.bool,

    /**
     * 	If true, the list item will be disabled.
     */
    disabled: PropTypes.bool,

    /**
     * 	If true, the left and right padding is removed.
     */
    disableGutters: PropTypes.bool,

    /**
     * 	If true, a 1px light border is added to the bottom of the list item.
     */
    divider: PropTypes.bool,

    /**
     * Use to apply selected styling.
     */
    selected: PropTypes.bool,

    /**
     * 	The main content element.
     */
    primary: PropTypes.string,

    /**
     * 	The secondary content element.
     */
    secondary: PropTypes.string,

    /**
     * 	Icon of the item
     */
    icon: PropTypes.string,

    /**
     * 	Avatar icon of the item
     */
    avatarIcon: PropTypes.string,

    /**
     * 	If true, the children will be indented.
     */
    inset: PropTypes.bool,

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
