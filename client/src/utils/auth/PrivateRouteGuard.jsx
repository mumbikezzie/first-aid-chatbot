import PropTypes from 'prop-types';
import { Navigate} from 'react-router-dom';

export const PrivateRouteGuard = ({children}) => {
  const access_token = window.localStorage.getItem('first_aid_access_token');
  if (!access_token) {
    return <Navigate to="/login"/>
  }

  return children;
};

PrivateRouteGuard.propTypes = {
  children: PropTypes.node.isRequired,
};