import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { fetchFilms } from "../../thunks/filmThunks";

function FilmCarousel() {
  const dispatch = useDispatch();
  const films = useSelector(state => state.film.films); // Assuming your reducer stores films in the state

  // Use local state to manage loading and error states
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        setError(null);
        await dispatch(fetchFilms()); // Assuming fetchFilms is your thunk
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [dispatch]);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div>
      <h1>Film List</h1>
      <ul>
        {films?.map(film => (
          <li key={film.id}>{film.title}</li>
        ))}
      </ul>
    </div>
  );
};


export default FilmCarousel
