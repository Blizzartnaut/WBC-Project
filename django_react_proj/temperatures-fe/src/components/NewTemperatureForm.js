import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewTemperatureForm extends React.Component {
    state = {
        pk: 0,
        date: "",
        time: "",
        burnerzone: "",
        burner_1: "",
        burner_2: "",
        burner_3: "",
        burner_4: "",
        burner_5: "",
        burner_6: "",
        burner_7: "",
        burner_8: "",
        burner_9: "",
        burner_10: "",
        burner_11: "",
        burner_12: "",
        user: ""
    };

    componentDidMount() {
        if (this.props.temperatures) {
            const { pk, date, time, burnerzone, burner_1, burner_2, burner_3, burner_4, burner_5, burner_6, burner_7, burner_8, burner_9, burner_10, burner_11, burner_12, user } = this.props.temperature;
            this.setState({ pk, date, time, burnerzone, burner_1, burner_2, burner_3, burner_4, burner_5, burner_6, burner_7, burner_8, burner_9, burner_10, burner_11, burner_12, user });
        }
    }

    onChange = e => {
        this.setState({ [e.target.name]: e.target.value });
    };

    createTemperature = e => {
        e.preventDefault();
        axios.post(API_URL, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    };

    editTemperature = e => {
        e.preventDefault();
        axios.put(API_URL + this.state.pk, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    };

    defaultIfEmpty = value => {
        return value === "" ? "" : value;
    };

    render() {
        return (
            <Form onSubmit={this.props.temperatures ? this.editTemperature : this.createTemperature}>
                <FormGroup>
                    <Label for="burnerzone">BurnerZone:</Label>
                    <Input
                        type="integer"
                        name="burnerzone"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burnerzone)}
                    />
                </FormGroup>                
                <FormGroup>
                    <Label for="burner_1">Burner 1 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_1"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_1)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="burner_2">Burner 2 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_2"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_2)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="burner_3">Burner 3 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_3"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_3)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="burner_4">Burner 4 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_4"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_4)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="burner_5">Burner 5 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_5"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_5)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="burner_6">Burner 6 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_6"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_6)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="burner_7">Burner 7 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_7"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_7)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="burner_8">Burner 8 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_8"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_8)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="burner_9">Burner 9 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_9"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_9)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="burner_10">Burner 10 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_10"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_10)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="burner_11">Burner 11 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_11"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_11)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="burner_12">Burner 12 Temperature:</Label>
                    <Input
                        type="text"
                        name="burner_12"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.burner_12)}
                    />
                </FormGroup>            
                <FormGroup>
                    <Label for="user">User:</Label>
                    <Input
                        type="text"
                        name="user"
                        onChange={this.onChange}
                        defaultValue={this.defaultIfEmpty(this.state.user)}
                    />
                </FormGroup>
                <Button>Send</Button>            
            </Form>
        );
    }
}

export default NewTemperatureForm;