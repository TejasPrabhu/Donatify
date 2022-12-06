/**@module getItemDetailAPI */

import axios from '../axios';

/**
 * API to get item details from database
 * @param {Number} value Id of the item to be queried
 * @returns {Promise} Response for axios GET request
 */
const getItemDetailAPI = (id) => {
	return axios.get(`/item?id=${id}`);
};
export default getItemDetailAPI;
