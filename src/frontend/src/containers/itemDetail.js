/**@module itemDetailContainer */

import { connect } from 'react-redux';
import ItemDetail from '../components/itemDetail';

/**
 * Map actions to props for marketplace component
 * @returns {Object} Actions object
 */
const mapDispatchToProps = () => {
	return {};
};

/**
 * Map state to props for marketplace component
 * @returns {Object} Props
 */
const mapStateToProps = () => ({
	userId: JSON.parse(localStorage.getItem('userLogonDetails')).userId
});

/**
 * Using connect, subscribe marketplace component to redux store
 */
export default connect(mapStateToProps, mapDispatchToProps)(ItemDetail);