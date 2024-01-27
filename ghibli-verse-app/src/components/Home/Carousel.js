import image1 from './images/princessmononoke.jpg'
import image2 from './images/spirited-away.jpg'


// import function to register Swiper custom elements
import { register } from 'swiper/element/bundle';
// register Swiper custom elements
register();

function Carousel() {
  return (
    <div>
      <swiper-container>
        <swiper-slide>
          <div>
            <img
              src={image1}
              alt='First carousel studio ghibli film'
            />
            <div class="absolute top-0 left-0 right-0 bottom-0 flex items-center justify-center">
              <p class="text-white text-2xl font-bold">Text Over Image 1</p>
            </div>
          </div>
        </swiper-slide>
        <swiper-slide>
          <div>
            <img
              src={image2}
              alt='First carousel studio ghibli film'
            />
            <div class="absolute top-0 left-0 right-0 bottom-0 flex items-center justify-center">
              <p class="text-white text-2xl font-bold">Text Over Image 2</p>
            </div>
          </div>
        </swiper-slide>
        <swiper-slide>
          Slide 3
        </swiper-slide>
      </swiper-container>
    </div>
  )
}

export default Carousel
