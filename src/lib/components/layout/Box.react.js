import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiBox from '@material-ui/core/Box';
import {omit} from "ramda";

/**
 * Box component from Material UI
 */
export default class Box extends Component {

    render() {

        const {
            id,
            children,
            style,
            className,
            ...otherProps
        } = this.props;

        return (
            <MuiBox href="#" css={style} className={className} {...omit(['setProps'], otherProps)}>
                {children}
            </MuiBox>
        )
    }

}

Box.defaultProps = {
};

Box.propTypes = {
    /**
     * The ID of this component.
     */
    id: PropTypes.string,

    /**
     * The content of the link.
     */
    children: PropTypes.node,

    /**
     * Override or extend the styles applied to the component.
     */
    className: PropTypes.object,

    /**
     * If true, the left and right padding is removed.
     */
    disableGutters: PropTypes.bool,

    /**
     * Set the max-width to match the min-width of the current breakpoint.
     */
    fixed: PropTypes.bool,

    /**
     * Determine the max-width of the container.
     */
    maxWidth: PropTypes.bool,

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
