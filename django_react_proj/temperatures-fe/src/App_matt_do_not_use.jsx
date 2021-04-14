import { useEffect, useState } from "react";
import { format } from "date-fns";

/**
 * A method that generates a resolved promise after the specified number of milliseconds.
 * @param {number} ms The number of milliseconds to wait until the promise resolves.
 * @returns {Promise} Returns a promise after the milliseconds have elapsed.
 */
const waitFor = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

/**
 * A method that fetches the data from the server.
 * @param {string} date The stringified date variable.
 * @returns {Promise} Returns a promise containing the fetch request that resolves when it's fetched the data from the server.
 */
const fetchData = (date) =>
	new Promise((resolve) => {
		fetch(`http://192.168.40.131:8000/api/temperatures/${date ? date.toString() : ""}`)
			.then((res) => res.json())
			.then(resolve);
	});

/**
 * The react hook that fetches the table data and updates the state of the requested data.
 * @param {string} date The stringified date variable.
 * @returns {[Array, Boolean]} Returns the data and a loading variable.
 */
const useTableData = (date) => {
	const [data, setData] = useState([]);
	const [loading, setLoading] = useState(true);

	useEffect(() => {
		setLoading(true);
		Promise.all([waitFor(1250), fetchData(date)]).then(([, data]) => {
			setData(data);
			setLoading(false);
		});
	}, [date]);

	return [data, loading];
};

const Loader = () => (
	<div className="flex items-center">
		Loading..{" "}
		<div class="lds-facebook">
			<div></div>
			<div></div>
			<div></div>
		</div>
	</div>
);

const Table = ({ data }) => (
	<table className="table-auto">
		<thead>
			<tr>
				<th>Date</th>
				<th>Temp</th>
			</tr>
		</thead>
		<tbody>
			{
				data.map((it, i) => (
					<tr className={i % 2 !== 0 ? "bg-gray-100" : ""}>
						<td className="p-2">{ format(new Date(it.date), "Pp") }</td>
						<td className="p-2">{ it.temp }</td>
					</tr>
				))
			}
		</tbody>
	</table>
);

const NoResults = () => (
	<div className="font-semibold text-2xl">No Results Found</div>
)

function App() {
	const [date, setDate] = useState();
	const [data, loading] = useTableData(date);

	/**
	 * A method that handles the date input field "changed" event.
	 * @param {*} e The HTML Event of the input.
	 */
	const handleDateChange = (e) => {
		const date = e.target.value;
		setDate(date);
	};

	return (
		<div className="max-w-6xl mx-auto my-10">
			<header>
				<h1 className="text-6xl font-semibold">Temps</h1>
				<div className="inline-flex py-2 px-3 items-center rounded my-3 border">
					<label htmlFor="filter" className="mr-3">
						Search By:
					</label>
					<input
						onChange={handleDateChange}
						type="date"
						name="filter"
						id="filter"
					/>
				</div>
			</header>
			<div className="mt-5">
				{loading && <Loader />}
				{!loading && (data.length ? <Table data={data}/> : <NoResults />)}
				</div>
		</div>
	);
}

export default App;
