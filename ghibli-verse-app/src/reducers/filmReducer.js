import {
  FETCH_FILMS_REQUEST,
  FETCH_FILMS_SUCCESS,
  FETCH_FILMS_FAILURE,
} from '../actions/filmActions';

const initialState = {
    films: [],
    loading: false,
    error: null,
}

const filmReducer = (state = initialState, action) => {
  switch (action.type) {
    case FETCH_FILMS_REQUEST:
      return { ...state, loading: true, error: null };

    case FETCH_FILMS_SUCCESS:
      return { ...state, films: action.payload, loading: false, error: null };

    case FETCH_FILMS_FAILURE:
      return { ...state, loading: false, error: action.payload };

    default:
      return state;
  }
};

export default filmReducer;
