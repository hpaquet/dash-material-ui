import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {omit} from 'ramda';
import MuiFormControl  from '@material-ui/core/FormControl';
import {withStyles} from "@material-ui/core/styles";


/**
 * FormControl component from Material UI
 */
export default class FormControl extends Component {

    render() {
        const {
            customStyle,
            ...otherProps
        } = this.props;

        if (customStyle){
            const CustomFormControl = withStyles(customStyle)(MuiFormControl);
            return (
                <>
                    <CustomFormControl {...omit(['setProps'], otherProps)}>
                        {this.props.children}
                    </CustomFormControl>
                </>
            );
        }

        return (
            <>
                <MuiFormControl {...omit(['setProps'], otherProps)}>
                    {this.props.children}
                </MuiFormControl>
            </>
        );
    }

}

FormControl.defaultProps = {
};

FormControl.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Style to apply to the component container.
     */
    style: PropTypes.object,

    /**
     * Custom FormControl style to apply to the component.
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
     * The component used for the root node.
     */
    component: PropTypes.string,

    /**
     * If true, the FormControl will be disabled.
     */
    disabled: PropTypes.bool,

    /**
     * If true, the label should be displayed in an error state.
     */
    error: PropTypes.bool,

    /**
     * If true, the component will be displayed in focused state.
     */
    focused: PropTypes.bool,

    /**
     * If true, the FormControl will take up the full width of its container.
     */
    fullWidth: PropTypes.node,

    /**
     * If true, the label will be hidden.
     */
    hiddenLabel: PropTypes.bool,

    /**
     * If dense or normal, will adjust vertical spacing of this and contained components.
     */
    margin: PropTypes.string,

    /**
     * 	If true, the label will indicate that the input is required.
     */
    required: PropTypes.string,

    /**
     * The size of the FormControl.
     */
    size: PropTypes.string,

    /**
     * The variant to use.
     */
    variant: PropTypes.string,

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
