import { configureStore } from '@reduxjs/toolkit';
import filmReducer from '../reducers/filmReducer';

const store = configureStore({
  reducer: {
    film: filmReducer,
    // Add other reducers if needed
  },
  // Add middleware, devTools, or other configuration options here
});

export default store;
