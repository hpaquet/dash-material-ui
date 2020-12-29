import React, {Component} from 'react';
import PropTypes from 'prop-types';
import MUIRadio from '@material-ui/core/Radio';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import RadioGroup from '@material-ui/core/RadioGroup';
import FormControl from '@material-ui/core/FormControl';
import {omit} from "ramda";

/**
 * Radio component from Material UI
 */
export default class Radio extends Component {

    constructor(props) {
        super(props);

        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.props.setProps({
            checked: event.target.checked,
            checked_timestamp: Date.now()
        });
    }

    render() {

        const {
            label,
            color,
            value,
            disableRipple,
            required,
            checked_timestamp,
            labelPlacement,
            ...otherProps
        } = this.props;

        if (label) {

            const radioButton = <MUIRadio
                                    color={color}
                                    disableRipple={disableRipple}
                                    required={required}
                                    checked_timestamp={checked_timestamp}
                                />

            return (
                <FormControl>
                    <RadioGroup >
                        <FormControlLabel
                            onChange={this.handleChange}
                            control={radioButton}
                            label={label}
                            labelPlacement={labelPlacement}
                            {...omit(['setProps'], otherProps)}
                        />
                    </RadioGroup>
                </FormControl>
            )
        }

        return (
                <MUIRadio
                    color={color}
                    onChange={this.handleChange}
                    disableRipple={disableRipple}
                    required={required}
                    checked_timestamp={checked_timestamp}
                    {...omit(['setProps'], otherProps)}
                />
            )
    }

}

Radio.defaultProps = {
    checked: false,
    checked_timestamp: -1
};

Radio.propTypes = {
    /**
     * The ID of this component.
     */
    id: PropTypes.string,

    /**
     * If true, the component is checked.
     */
    checked: PropTypes.bool,

    /**
     * Timestamp of the last time the component as been clicked on.
     */
    checked_timestamp: PropTypes.number,

    /**
     * Override or extend the styles applied to the component.
     */
    classes: PropTypes.object,

    /**
     * The color of the component.
     */
    color: PropTypes.string,

    /**
     * If true, the switch will be disabled.
     */
    disabled: PropTypes.bool,

    /**
     * If true, the ripple effect will be disabled.
     */
    disableRipple: PropTypes.bool,

    /**
     *  The text to be used in an enclosing label element.
     */
    label: PropTypes.string,

    /**
     * 	The position of the label.
     */
    labelPlacement: PropTypes.string,

    /**
     * 	Name attribute of the input element.
     */
    name: PropTypes.string,

    /**
     * The size of the switch.
     */
    size: PropTypes.string,

    /**
     * The style of the switch.
     */
    style: PropTypes.object,

    /**
     * If true, the input element will be required.
     */
    required: PropTypes.bool,

    /**
     * The value of the component.
     */
    value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
