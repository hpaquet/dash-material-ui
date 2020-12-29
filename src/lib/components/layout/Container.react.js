import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiContainer from '@material-ui/core/Box';
import {omit} from "ramda";

/**
 * Container component from Material UI
 */
export default class Container extends Component {

    render() {

        const {
            id,
            children,
            style,
            className,
            ...otherProps
        } = this.props;

        return (
            <MuiContainer href="#" css={style} className={className} onClick={this.preventDefault} {...omit(['setProps'], otherProps)}>
                {children}
            </MuiContainer>
        )
    }

}

Container.defaultProps = {
};

Container.propTypes = {
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
     * The style of the text field.
     */
    style: PropTypes.string,

    /**
     * If true, the box will recycle its children DOM element.
     */
    clone: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
