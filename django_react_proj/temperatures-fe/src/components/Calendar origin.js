import "flatpickr/dist/themes/material_green.css";

import Flatpickr from "react-flatpickr";
import { Component } from "react";

export default class Calendar extends Component {
  constructor(props) {
    super(props);

    this.state = {
      date: new Date()
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
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