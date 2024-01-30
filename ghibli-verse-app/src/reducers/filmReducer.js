// import { INCREMENT, DECREMENT } from '../constants/actionTypes'; //! ACTIONS WIP
import { FETCH_FILMS } from "../constants/filmConstants";

const initialState = { films: {} }

const filmReducer = (state = initialState, action) => {
  switch (action.type) {
    case FETCH_FILMS:
      return { films: { ...action.films } }
    default:
      return state;
  }
};

export default filmReducer;
