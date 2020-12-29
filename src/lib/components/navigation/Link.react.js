import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MuiLink from '@material-ui/core/Link';
import {omit} from "ramda";

/**
 * Link component from Material UI
 */
export default class Link extends Component {

    constructor(props) {
        super(props);

        this.preventDefault = this.preventDefault.bind(this);
    }

    preventDefault(event) {
        event.preventDefault();
    }

    render() {

        const {
            id,
            children,
            ...otherProps
        } = this.props;

        return (
            <MuiLink href="#" onClick={this.preventDefault} {...omit(['setProps'], otherProps)}>
                {children}
            </MuiLink>
        )
    }

}

Link.defaultProps = {
};

Link.propTypes = {
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
    classes: PropTypes.object,

    /**
     * The color of the component.
     */
    color: PropTypes.string,

    /**
     * Classes prop applied to the Typography element.
     */
    TypographyClasses: PropTypes.object,

    /**
     * Controls when the link should have an underline.
     */
    underline: PropTypes.string,

    /**
     * The style of the text field.
     */
    style: PropTypes.string,

    /**
     * The variant to use.
     */
    variant: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
