// Action types
export const FETCH_FILMS_REQUEST = 'FETCH_FILMS_REQUEST';
export const FETCH_FILMS_SUCCESS = 'FETCH_FILMS_SUCCESS';
export const FETCH_FILMS_FAILURE = 'FETCH_FILMS_FAILURE';

// Action creators
export const fetchFilmsRequest = () => ({
  type: FETCH_FILMS_REQUEST,
});

export const fetchFilmsSuccess = (films) => ({
  type: FETCH_FILMS_SUCCESS,
  payload: films.films,
});

export const fetchFilmsFailure = (error) => ({
  type: FETCH_FILMS_FAILURE,
  payload: error,
});
