import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchFilms } from "../../thunks/filmThunks";


function AllFilms() {
  const dispatch = useDispatch();
  const films = useSelector(state => state.film.films);

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
    <div className="grid grid-cols-4 gap-4 justify-items-center mt-20">
      {films.map(film => (
        <div>
          <img
            src={film.imageURL}
            alt={film.id}
            className="h-3/6"
            />
          <p>{film.title}</p>
        </div>
        ))}
    </div>
  )
}

export default AllFilms;
