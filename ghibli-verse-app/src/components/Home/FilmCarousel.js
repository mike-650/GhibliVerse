import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { fetchFilms } from "../../thunks/filmThunks";

function FilmCarousel() {
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
    <div>
      <swiper-container
        navigation='true'
        pagination='true'
        slides-per-view="3"
        slides-per-group="3"
        space-between="100px"
        >
        {films.map(film => (
          <swiper-slide key={film.id}>
            <img src={film.imageURL} alt={film.title} />
          </swiper-slide>
        ))}
      </swiper-container>
    </div>
  );
};


export default FilmCarousel
