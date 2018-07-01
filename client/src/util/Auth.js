
import axios from 'axios';
import store from '../store';
import setToken from '../actions/index';
import { URL, LOGIN } from '../config/Api';
import AppConstants from '../constants/AppConstants';

export const InvalidCredentialsException = (message) => {
  this.message = message;
  this.name = 'InvalidCredentialsException';
};


export const login = (username, password) => (
  axios
    .post(URL + LOGIN, { username, password })
    .then((response) => {
      store.dispatch(setToken(response.data.token));
    })
    .catch((error) => {
      const data = error.response;
      store.dispatch({ type: AppConstants.SET_TOKEN_ERROR, data });
    })
);

export const loggedIn = () => store.getState().token == null;
