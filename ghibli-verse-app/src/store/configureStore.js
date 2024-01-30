import { configureStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk'; // For handling asynchronous actions
import logger from 'redux-logger'; // For logging actions and state changes
// import rootReducer from '../reducers';

const middlewares = [thunk, logger]; // Add other middleware as needed

const createStore = () => {
  const store = configureStore(
    combineReducers({
      // Add reducers here
      // For example: counter: counterReducer
    }),
    applyMiddleware(...middlewares)
  );

  return store;
};

export default createStore;
