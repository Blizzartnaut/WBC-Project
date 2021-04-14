import React, { Component } from "react";
import { Table } from "reactstrap";
import NewTemperatureModal from "./NewTemperatureModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class TemperatureList extends Component {
    render() {
        const temperatures = this.props.temperatures;
        return (
            <Table dark>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Time</th>
                        <th>BurnerZone</th>
                        <th>Burner 1</th>
                        <th>Burner 2</th>
                        <th>Burner 3</th>
                        <th>Burner 4</th>
                        <th>Burner 5</th>
                        <th>Burner 6</th>
                        <th>Burner 7</th>
                        <th>Burner 8</th>
                        <th>Burner 9</th>
                        <th>Burner 10</th>
                        <th>Burner 11</th>
                        <th>Burner 12</th>
                        <th>User</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {!temperatures || temperatures.length <= 0 ? (
                        <tr>
                            <td colSpan = "6" align = "center">
                                <b>No temperatures assigned yet</b>
                            </td>
                        </tr>
                    ) : (
                        temperatures.map(temperature => (
                            <tr key = {temperature.pk}>
                                <td>{temperature.date}</td>
                                <td>{temperature.time}</td>
                                <td>{temperature.burnerzone}</td>
                                <td>{temperature.burner_1}</td>    
                                <td>{temperature.burner_2}</td>
                                <td>{temperature.burner_3}</td>
                                <td>{temperature.burner_4}</td>
                                <td>{temperature.burner_5}</td>
                                <td>{temperature.burner_6}</td>
                                <td>{temperature.burner_7}</td>
                                <td>{temperature.burner_8}</td>
                                <td>{temperature.burner_9}</td>
                                <td>{temperature.burner_10}</td>
                                <td>{temperature.burner_11}</td>
                                <td>{temperature.burner_12}</td>
                                <td>{temperature.user}</td>
                                <td align = "center">
                                    <NewTemperatureModal
                                        create={false}
                                        temperature={temperature}
                                        resetState={this.props.resetState}
                                    />
                                    &nbsp;&nbsp;
                                    <ConfirmRemovalModal
                                        pk={temperature.pk}
                                        resetState={this.props.resetState}
                                    />
                                </td>
                            </tr>
                        ))
                    )}
                </tbody>
            </Table>
        );
    }
}

export default TemperatureList;