
import { compose, createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { createLogger } from 'redux-logger';
import { persistStore } from 'redux-persist';
import rootReducer from './reducers/AppReducers';

const store = createStore(
  rootReducer,
  compose(
    applyMiddleware(createLogger(), thunk),
    window.devToolsExtension ? window.devToolsExtension() : func => func
  ),
);
persistStore(store);

export default store;
