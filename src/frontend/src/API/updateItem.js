/**@module updateItemAPI */

import axios from '../axios';

/**
 * API to book the item
 * @param {Object} value Object containing item details
 * @returns {Promise} Response for axios PUT request
 */
const updateItemAPI = (data) => {
	console.log(data);
	return axios.put('/updateitem', {
		...data
	});
};
export default updateItemAPI;
