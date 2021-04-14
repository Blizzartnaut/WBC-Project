import "flatpickr/dist/themes/material_green.css";

import Flatpickr from "react-flatpickr";
import React, { Component } from "react";
import axios from "axios";
import { API_URL } from "../constants";

export default class Calendar extends Component {
  constructor(props) {
    super(props);

    this.state = {
      date: new Date()
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  state = {
    listTemperatures: []
  }

  componentDidMount() {
    axios.get(API_URL).then(response => {
      const temperatures = response.data;
        this.setState ({temperatures});
    })
  }

  handledChange(date) {
    this.setState({
      date: Event.target.value
    })
  }

  handleChange(event) {
    this.setState({date: event.target.value});
  }

  handleSubmit(event) {
    alert('A date was submitted: ' + this.state.date);
    event.preventDefault();
  }

  render() {
    const { date } = this.state;
    return (
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
    );
  }
}

//export default App;