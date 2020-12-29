import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {omit} from 'ramda';
import MuiFormControlLabel  from '@material-ui/core/FormControlLabel';
import {withStyles} from "@material-ui/core/styles";


/**
 * FormControlLabel component from Material UI
 */
export default class FormControlLabel extends Component {

    constructor(props) {
        super(props);

        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.props.setProps({checked: event.target.checked});
    }

    render() {
        const {
            customStyle,
            ...otherProps
        } = this.props;

        if (customStyle){
            const CustomFormControlLabel = withStyles(customStyle)(MuiFormControlLabel);
            return (
                <>
                    <CustomFormControlLabel onChange={this.handleChange} control={this.props.children} {...omit(['setProps'], otherProps)} />
                </>
            );
        }

        return (
            <>
                <MuiFormControlLabel onChange={this.handleChange} control={this.props.children} {...omit(['setProps'], otherProps)} />
            </>
        );
    }

}

FormControlLabel.defaultProps = {
};

FormControlLabel.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Style to apply to the component container.
     */
    style: PropTypes.object,

    /**
     * If true, the component is checked.
     */
    checked: PropTypes.bool,

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
     * If true, the FormControl will be disabled.
     */
    disabled: PropTypes.bool,

    /**
     * The position of the label.
     */
    labelPlacement: PropTypes.string,

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
