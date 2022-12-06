import React, { Component } from 'react';
import getDonorHistoryAPI from '../API/getDonorHistory';
import getRecipientHistoryAPI from '../API/getRecipientHistory';
import { Avatar, Radio, Card } from 'antd';
import { Modal as ViewModal} from 'antd';
import { Modal as EditModal} from 'reactstrap';
import { Button, ModalHeader, ModalBody, ModalFooter, FormGroup, Form, Input } from 'reactstrap';
import Select from 'react-select';
import makeAnimated from 'react-select/animated';
import updateItemAPI from '../API/updateItem';

const { Meta } = Card;

/**
 * React component for showing user donation and receive history
 * @extends React.Component
 */
class History extends Component {
	/**
	 * Set initial state
	 * @param {Object} props Props for the component
	 */
	constructor(props) {
		super(props);
		this.state = {
			donorHistory: [],
			recipientHistory: [],
			history: 'All',
			isModalOpen: false,
			isEditModalOpen: false,
			itemData:{
				itemId:'',
				itemName: '',
				itemQuantity: 1,
				itemDescription: '',
				itemZipCode: '',
				itemCity: {},
				itemDonorId: props.props && props.props.userId,
				itemCategory: {},
			},
			options: [
				{
					label: 'All',
					value: 'All',
				},
				{
					label: 'Donate History',
					value: 'Donate History',
				},
				{
					label: 'Bidding History',
					value: 'Bidding History',
				},
			]
		};
	}

	/**
	 * Get donor and receiver history from database and save it to state
	 */
	loadHistory = async () => {
		let userId = JSON.parse(localStorage.getItem('userLogonDetails')).userId;
		const donorHistoryResponse = await getDonorHistoryAPI(userId);
		if (donorHistoryResponse.data && donorHistoryResponse.data.data) {
			this.setState({
				...this.state,
				donorHistory: donorHistoryResponse.data.data,
			});
		}

		const recipientHistoryResponse = await getRecipientHistoryAPI(userId);
		if (recipientHistoryResponse.data && donorHistoryResponse.data.data) {
			this.setState({
				...this.state,
				recipientHistory: recipientHistoryResponse.data.data
			});
		}
		return true;
	};

	handleSave = async (event) => {
		// Validate if input values are empty
		const keys = ['itemName', 'itemDescription', 'itemZipCode'];
		for (let i = 0; i < keys.length; i++) {
			if (this.state.itemData[keys[i]] === '') {
				alert(`Missing value for ${keys[i]}. Please enter the required information`);
				return false;
			}
		}
		event.preventDefault();
		if (Object.keys(this.state.itemData.itemCity).length === 0) {
			alert('Missing value for city. Enter city for the item.');
			return false;
		}
		if (Object.keys(this.state.itemData.itemCategory).length === 0) {
			alert('Missing value for category. Enter category for the item.');
			return false;
		}
		let res = await updateItemAPI(this.state.itemData);
		if (res.data&&res.data.status===200) {
			alert('Item updated successfully');
			await this.loadHistory();
			this.setIsEditModalOpen(false);
			this.handleEditSave();
			return true;
		}

		return false;
	};

	// /**
	//  * Load next page results
	//  */
	// loadMore = () => {
	// 	this.setState(
	// 		prevState => ({
	// 			page: prevState.page + 1,
	// 			scrolling: true
	// 		}),
	// 		this.loadHistory
	// 	);
	// };

	/**
	 * Lifecycle method to trigger loading history
	 */
	componentDidMount = async () => {
		await this.loadHistory();
	};

	/**
	 * Update state with type of history required
	 * @param {Object} event onChange event for user input
	 */
	setHistory = (event) => {
		this.setState({
			history: event.target.value
		});
		return true;
	};

	/**
	 * Set modal display to be true
	 * @param {Boolean} value True to display the modal, false otherwise
	 */
	setIsModalOpen = (value) => {
		this.setState({
			isModalOpen: value
		});
		return true;
	};

	setIsEditModalOpen = (value) => {
		this.setState({
			isEditModalOpen: value
		});
		return true;
	};

	handleEditSave = () => {
		this.setIsEditModalOpen(false);
	};

	/**
	 * Hide model when Cancel button clicked
	 */
	handleEditCancel = () => {
		this.setIsEditModalOpen(false);
	};

	handleInput = (event) => {

		if (event.type === 'change') {
			if (event.target) {
				this.setState({
					...this.state,
					itemData: {
						...this.state.itemData,
						[event.target.id]: event.target.value
					}
				});
			}
		} else {
			this.setState({
				...this.state,
				itemData: {
					...this.state.itemData,
					[event.name]: event.values.value
				}
			});
		}
	};

	/**
	 * Render History component
	 * @returns {React.Component} History related cards
	 */
	render() {
		const gridStyle = {
			width: '25%',
			textAlign: 'center',
		};

		/**
		 * Store selected item data in state and display model
		 * @param {Object} data Object containing item details
		 */
		const showModal = (data) => {
			console.log('inside view modal func');
			this.setState({
				d: {
					...data
				}
			});
			this.setIsModalOpen(true);
		};

		const showEditModal = (ID) => {
			this.setState({
				...this.state,
				itemData: {
					...this.state.itemData,
					itemId: ID
				}
			});
			this.setIsEditModalOpen(true);
		};

		/**
		 * Hide modal when OK button clicked
		 */
		const handleOk = () => {
			this.setIsModalOpen(false);
		};

		/**
		 * Hide model when Cancel button clicked
		 */
		const handleCancel = () => {
			this.setIsModalOpen(false);
		};

		const cities = [
			{
				label: 'Raleigh',
				value: 'raleigh'
			},
			{
				label: 'Cary',
				value: 'cary'
			},
			{
				label: 'Durham',
				value: 'durham'
			}
		];
		const interestItems = [
			{
				label: 'Fruits',
				value: 'fruits'
			},
			{
				label: 'Vegetables',
				value: 'vegetables'
			},
			{
				label: 'Table',
				value: 'table'
			},
			{
				label: 'Chair',
				value: 'chair'
			},
			{
				label: 'Chair1',
				value: 'chair1'
			},
			{
				label: 'Chair2',
				value: 'chair2'
			}
		];
		const animatedComponents = makeAnimated();

		return (
			<>

				{this.state.isModalOpen ? (<ViewModal title="Item Details" open={this.state.isModalOpen} onOk={handleOk} onCancel={handleCancel} onClick={e => e.stopPropagation}>

					<p>Item Name: {this.state.d.itemName}</p>
					<p>Item Quantity: {this.state.d.itemQuantity}</p>
					<p>Item Description: {this.state.d.itemDescription}</p>
					<p>Item Zip Code: {this.state.d.itemZipCode}</p>
					<p>Item City: {this.state.d.itemCity}</p>
					<p>Item Category: {this.state.d.itemCategory}</p>

					{!this.state.history==='Donate History'?(<p>Donor Name: {this.state.d.itemDonorName || ''}</p>):(<></>)}
				</ViewModal>) : (<></>)}
				{console.log('again')}
				{console.log(this.state.isModalOpen)}
				{this.state.isEditModalOpen ? (
					// toggle={this.toggle}>
					<EditModal isOpen={this.state.isEditModalOpen}>
						<ModalHeader toggle={this.toggle}>Edit Item</ModalHeader>
						<ModalBody>
							<Form>
								<FormGroup>
									{/* <Label> */}
									Item Name
									{/* </Label> */}
									<Input
										type='name'
										name='name'
										id='itemName'
										placeholder='Item name'
										defaultValue={this.state.itemData.itemName}
										onChange={this.handleInput}
									/>
								</FormGroup>
								<FormGroup>
									{/* <Label for="password"> */}
									Item Description
									{/* </Label> */}
									<Input
										name='description'
										type='textarea'
										id='itemDescription'
										placeholder='Item description'
										defaultValue={this.state.itemData.itemDescription}
										onChange={this.handleInput}
									/>
								</FormGroup>
								<FormGroup>
									{/* <Label for="password"> */}
									Item Quantity
									{/* </Label> */}
									<Input
										type='text'
										name='quantity'
										id='itemQuantity'
										placeholder='Item quantity'
										defaultValue={this.state.itemData.itemQuantity}
										onChange= {(event) => this.handleInput(event)}
									/>
								</FormGroup>
								<FormGroup>
									{/* <Label for="password"> */}
									Zip Codes
									{/* </Label> */}
									<Input
										type='text'
										name='zipcode'
										id='itemZipCode'
										placeholder='Item zipcode'
										defaultValue={this.state.itemData.itemZipCode}
										onChange={this.handleInput}
									/>
								</FormGroup>
								<FormGroup>
									{/* <Label for="password"> */}
									City
									{/* </Label> */}
									<Select
										id='itemCity'
										closeMenuOnSelect={true}
										components={animatedComponents}
										options={cities}
										placeholder={'City'}
										maxMenuHeight={200}
										menuPlacement='top'
										name='itemCity'
										defaultValue={this.state.itemData.itemCity}
										onChange={(event) => this.handleInput({values: event, name: 'itemCity'})}
									/>
								</FormGroup>
								<FormGroup>
									{/* <Label for="password"> */}
									Item Category
									{/* </Label> */}
									<Select
										id='itemCategory'
										closeMenuOnSelect={true}
										components={animatedComponents}
										options={interestItems}
										placeholder={'Category'}
										maxMenuHeight={200}
										menuPlacement='top'
										name='itemCategory'
										defaultValue={this.state.itemData.itemCategory}
										onChange={(event) => this.handleInput({values: event, name: 'itemCategory'})}
									/>
								</FormGroup>
							</Form>
						</ModalBody>
						<ModalFooter>
							<Button color="primary" onClick={event => this.handleSave(event)}>
								Save
							</Button>{' '}
							<Button color="secondary" onClick={this.handleEditCancel}>
								Cancel
							</Button>
						</ModalFooter>
					</EditModal>
				) : (<></>)}

				{/* <Modal title="Item Details" open={this.state.isModalOpen} onOk={handleOk} onCancel={handleCancel}>
          <p>Item Name: {d.itemName}</p>
          <p>Item Quantity: {d.itemQuantity}</p>
          <p>Item Description: {d.itemDescription}</p>
          <p>Item Zip Code: {d.itemZipCode}</p>
          <p>Item City: {d.itemCity}</p>
          <p>Donor Name: {d.itemDonorName}</p>
          <p>Item Category: {d.itemCategory}</p>
        </Modal> */}
				<Radio.Group options={this.state.options} onChange={this.setHistory} value={this.state.history} optionType="button" buttonStyle="solid" />
				<Card title={this.state.history}>
					{((this.state.history === 'All' || this.state.history === 'Donate History') && this.state.donorHistory.length > 0) ?
						this.state.donorHistory.map((donor) => (
							<Card.Grid style={gridStyle}>
								<Card
									style={{
										width: '100%',
									}}
									cover={
										<img
											alt="example"
											src={(donor.imgName !== '') ? 'http://127.0.0.1:8080/'.concat(donor.imgName) : 'https://picsum.photos/300/200'}
										/>
									}
								// actions={[
								//   <FolderViewOutlined key="view" />
								// ]}
								>
									<Meta
										avatar={<Avatar src="https://joeschmoe.io/api/v1/random" />}
										title={donor.itemName}
										description={donor.itemDescription}
									/>
									<Button type="primary" onClick={() => showModal(donor)}
										style={{ margin: 20 }}>
										View Details
									</Button>
									<Button type="primary" onClick= {() => showEditModal(donor.itemId)}>
										Edit Details
									</Button>

								</Card>
							</Card.Grid>
						))
						:
						(<div></div>)
					}
					{((this.state.history === 'All' || this.state.history === 'Bidding History') && this.state.recipientHistory.length > 0) ?
						this.state.recipientHistory.map((d) => (
							<Card.Grid style={gridStyle}>
								<Card
									style={{
										width: '100%',
									}}
									cover={
										<img
											alt="example"
											src="https://picsum.photos/300/200"
										/>
									}
								// actions={[
								//   <FolderViewOutlined key="view" />
								// ]}
								>
									<Meta

										//avatar={<Avatar src="https://joeschmoe.io/api/v1/random" />}
										title={d.itemName}
										description={d.itemDescription}
									/>
									<Button type="primary"onClick={() => showModal(d)}>
										View Details
									</Button>

								</Card>
							</Card.Grid>
						))
						:
						(<div></div>)
					}
				</Card>
			</>);
	}
}

export default History;
