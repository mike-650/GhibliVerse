import { fetchFilmsRequest, fetchFilmsSuccess, fetchFilmsFailure } from '../actions/filmActions';

export const fetchFilms = () => {
  return async (dispatch) => {
    dispatch(fetchFilmsRequest());

    try {
      const response = await fetch('/api/films');  // Adjust the endpoint based on your API
      const data = await response.json();
      dispatch(fetchFilmsSuccess(data));
    } catch (error) {
      dispatch(fetchFilmsFailure(error.message));
    }
  };
};
