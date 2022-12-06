/**@module addBidderApi */

import axios from '../axios';

/**
 * API to add item to the backend database
 * @param {Object} value Object to be inserted into database
 * @returns {Promise} Response for axios POST request
 */
const addBidderApi = (item_id, recipient_id) => {
	return axios.post('/addDonation', {
		recipient_id: recipient_id,
		item_id: item_id,
	});
};
export default addBidderApi;
