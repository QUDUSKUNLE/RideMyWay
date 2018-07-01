
import AppConstants from '../constants/AppConstants';
import initialState from '../app/initialState';

export const token = (state = initialState.tokenInitialState, action) => {
  switch (action.type) {
    case AppConstants.SET_TOKEN:
      return action.data;

    case AppConstants.SET_TOKEN_ERROR:
      return null;

    default:
      return state;
  }
};

export const signup = (state = initialState.register, action) => {
  switch (action.type) {
    case AppConstants.SIGNUP_SUCCESS:
      return action.data;

    case AppConstants.SIGNUP_ERROR:
      return action.data;

    default:
      return state;
  }
};
