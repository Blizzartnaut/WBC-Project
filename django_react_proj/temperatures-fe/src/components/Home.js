import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import TemperatureList from "./TemperatureList";
import NewTemperatureModal from "./NewTemperatureModal";

import "flatpickr/dist/themes/material_green.css";
import Flatpickr from "react-flatpickr";
import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
    state = {
        temperatures: []
    };

    componentDidMount() {
        this.resetState();
    }

    getTemperatures = () => {
        axios.get(API_URL).then(res => this.setState({ temperatures: res.data }));
    };

    resetState = () => {
        this.getTemperatures();
    };

    render() {
        const { date } = this.state;
        return (
            <Container style={{ marginTop: "20px" }}>
                <Row>
                    <Col>
                    <center>
                        <form onSubmit={this.handleSubmit}>
                            <label>
                              <Flatpickr
                                id='q'
                                value={date}
                                onChange={date => {
                                  this.setState({ date });
                                }}
                                />
                            </label>
                            <input type="submit" value="Submit" />
                        </form>
                    </center>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <TemperatureList
                            temperatures={this.state.temperatures}
                            resetState={this.resetState}
                        />
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <NewTemperatureModal create={true} resetState={this.resetState} />
                    </Col>
                </Row>
            </Container>
        );
    }
}

export default Home;