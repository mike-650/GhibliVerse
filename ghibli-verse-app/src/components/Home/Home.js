import Carousel from "./Carousel";
import FilmCarousel from "./FilmCarousel";
import NavigationBar from "./Navigation";

function Home() {
  return (
    <div>
      <NavigationBar />
      <Carousel />
      <FilmCarousel />
    </div>
  )
}

export default Home
