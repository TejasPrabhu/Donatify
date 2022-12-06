import React, { Component } from 'react';
import getItemDetailAPI from '../API/getItemDetail';
/**
 * React component for receiving component
 * @extends React.Component
 */

class ItemDetail extends Component {
	/**
	 * Set initial state
	 * @param {Object} props Props for the component
	 */
	constructor(props) {
		super(props);
		this.state = {
			itemDetail: {},
			showAlert: false,
			item_id: window.location.pathname.split('/')[3],
		};
	}
	loadData = async () => {
		let res = await getItemDetailAPI(this.state.item_id);
		console.log(res);
		if (res.data && res.data.data) {
			this.setState({
				...this.state,
				itemDetail: {
					item_id: res.data.data.item_id,
					item_name: res.data.data.item_name,
					quantity: res.data.data.quantity,
					description: res.data.data.description,
					zipcode: res.data.data.zipcode,
					city: res.data.data.city,
					category: res.data.data.category,
					donor_id: res.data.data.donor_id
				},
			});
			return true;
		}
		alert('No response from the server');
		return false;
	};
	/**
	 * Lifecycle method to trigger loading available items
	 */
	componentDidMount = async () => {
		// console.log(this.state)
		console.log(this.props);
		await this.loadData();
	};


	/**
	 * Render receiving component
	 * @returns {React.Component} Cards with available items
	 */
	render() {
		return (
			<section>
				<div className='container' style={{ padding: 10, margin: 5 }}>

					<h2>{this.state.itemDetail.item_name}</h2>

					<p>Description: {this.state.itemDetail.description}</p>

					<p>Quantity: {this.state.itemDetail.quantity}</p>

					<p>Category: {this.state.itemDetail.category}</p>

					<p>Zipcode: {this.state.itemDetail.zipcode}</p>

					<p>City: {this.state.itemDetail.city}</p>



				</div >
				<div className='container' style={{ padding: 10, margin: 5 }}>
					<h3>Comments</h3>
				</div>
			</section >);
	}
}
// App();
export default (ItemDetail);