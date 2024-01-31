import { fetchFilmsRequest, fetchFilmsSuccess, fetchFilmsFailure } from '../actions/filmActions';
import developmentConfig from '../config/development'

export const fetchFilms = () => {
  return async (dispatch) => {
    dispatch(fetchFilmsRequest());

    try {
      const response = await fetch(`http://localhost:5000/api/films/`);
      console.log(response)
      const data = await response.json();
      console.log(data)
      dispatch(fetchFilmsSuccess(data));
    } catch (error) {
      dispatch(fetchFilmsFailure(error.message));
    }
  };
};
