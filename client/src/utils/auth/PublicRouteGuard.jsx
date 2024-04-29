import { useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

export const PublicRouteGuard = ({ children, path }) => {
  const location = useLocation();
  const access_token = window.localStorage.getItem('jwt_access_token');
  const navigate = useNavigate();

  useEffect(() => {
    console.log({ pathname: location.pathname });
    const pathname = location.pathname;
    if (access_token && pathname === path) {
      navigate(-1);
    }
  });

  return children;
};