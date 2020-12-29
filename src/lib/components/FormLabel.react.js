import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {omit} from 'ramda';
import MuiFormLabel  from '@material-ui/core/FormLabel';
import {withStyles} from "@material-ui/core/styles";


/**
 * FormLabel component from Material UI
 */
export default class FormLabel extends Component {

    render() {
        const {
            customStyle,
            ...otherProps
        } = this.props;

        if (customStyle){
            const CustomFormLabel = withStyles(customStyle)(MuiFormLabel);
            return (
                <>
                    <CustomFormLabel {...omit(['setProps'], otherProps)}>
                        {this.props.children}
                    </CustomFormLabel>
                </>
            );
        }

        return (
            <>
                <MuiFormLabel {...omit(['setProps'], otherProps)}>
                    {this.props.children}
                </MuiFormLabel>
            </>
        );
    }

}

FormLabel.defaultProps = {
};

FormLabel.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Style to apply to the component container.
     */
    style: PropTypes.object,

    /**
     * The component used for the root node.
     */
    component: PropTypes.string,

    /**
     * Custom FormLabel style to apply to the component.
     */
    customStyle: PropTypes.object,

    /**
     * The content of the component.
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
     * If true, the FormLabel will be disabled.
     */
    disabled: PropTypes.bool,

    /**
     * If true, the label should be displayed in an error state.
     */
    error: PropTypes.bool,

    /**
     * 	If true, the label should use filled classes key.
     */
    filled: PropTypes.bool,

    /**
     * 		If true, the input of this label is focused (used by FormGroup components).
     */
    focused: PropTypes.node,

    /**
     * 	If true, the label will indicate that the input is required.
     */
    required: PropTypes.bool,

    /**
     * Class name to apply to the component.
     */
    className: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
