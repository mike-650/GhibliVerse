import image1 from './images/spirited-away.jpg';
import image2 from './images/princessmononoke.jpg';
import image3 from './images/ponyo.jpg';
import video from './videos/spirited-away.mp4'

// import function to register Swiper custom elements
import { register } from 'swiper/element/bundle';
// register Swiper custom elements
register();

function Carousel() {
  return (
    <div className='mb-40'>
      <swiper-container
        navigation='true'
        pagination='true'
        loop='true'
        // autoplay='{"delay":5000}'
        // UNCOMMENT TO ACTIVATE AUTOPLAY
      >
        <swiper-slide>
          <div>
            {/* <img
              src={image1}
              alt='First carousel studio ghibli film'
              className='cursor-pointer'
            /> */}
            <video autoPlay muted className='w-full'>
              <source src={video} type="video/mp4"/>
              "Your browser does not support the video tag."
            </video>
            <div className="absolute top-0 left-20 bottom-0 flex items-center justify-center w-80 bg-gray-900 bg-opacity-75">
              <p className="text-white text-2xl font-playfair font-bold">Spirited Away</p>
            </div>
          </div>
        </swiper-slide>
        <swiper-slide>
          <div>
            <img
              src={image2}
              alt='First carousel studio ghibli film'
              className='cursor-pointer'
            />
            <div className="absolute top-0 left-20 bottom-0 flex items-center justify-center w-80 bg-gray-900 bg-opacity-75">
              <p className="text-white text-2xl font-playfair font-bold">Princess Mononoke</p>
            </div>
          </div>
        </swiper-slide>
        <swiper-slide>
          <div>
            <img
              src={image3}
              alt='First carousel studio ghibli film'
              className='cursor-pointer'
            />
            <div className="absolute top-0 left-20 bottom-0 flex items-center justify-center w-80 bg-gray-900 bg-opacity-75">
              <p className="text-white text-2xl font-playfair font-bold">Ponyo</p>
            </div>
          </div>
        </swiper-slide>
      </swiper-container>
    </div>
  )
}

export default Carousel
