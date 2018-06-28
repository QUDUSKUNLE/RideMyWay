
import { combineReducers } from 'redux';
import { token, signup } from './index';

const appReducer = combineReducers({
  token,
  signup,
});

const rootReducer = (state, action) => appReducer(state, action);


export default rootReducer;
