import image1 from './images/spirited-away.jpg';
import image2 from './images/princessmononoke.jpg';
import image3 from './images/ponyo.jpg';
// import video from './videos/spirited-away.mp4'

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
            <img
              src={image1}
              alt='First carousel studio ghibli film'
              className='cursor-pointer'
            />
            <div className="absolute top-0 left-20 bottom-0 items-center justify-center w-72 bg-gray-900 bg-opacity-75 hidden lg:flex">
              <p className="text-white text-2xl font-playfair font-bold">Spirited Away</p>
              <div className="absolute bottom-20 ml-5 mr-5 text-center">
                <p className="text-white font-playfair font-light italic hidden xl:block">
                  "During her family's move to the suburbs,
                  a sullen 10-year-old girl wanders into a world ruled by gods,
                  witches and spirits, a world where humans are changed into beasts."
                </p>
              </div>
            </div>
          </div>
        </swiper-slide>
        <swiper-slide>
          <div>
            <img
              src={image2}
              alt='Second carousel studio ghibli film'
              className='cursor-pointer'
            />
            <div className="absolute top-0 left-20 bottom-0 items-center justify-center w-72 bg-gray-900 bg-opacity-75 hidden lg:flex">
              <p className="text-white text-2xl font-playfair font-bold">Princess Mononoke</p>
              <div className="absolute bottom-20 ml-5 mr-5 text-center">
              <p className="text-white font-playfair font-light italic hidden xl:block">
                "On a journey to find the cure for a Tatarigami's curse,
                Ashitaka finds himself in the middle of a war between the forest gods and Tatara,
                a mining colony. In this quest he also meets San, the Mononoke Hime."
              </p>
            </div>
            </div>
          </div>
        </swiper-slide>
        <swiper-slide>
          <div>
            <img
              src={image3}
              alt='Third carousel studio ghibli film'
              className='cursor-pointer'
            />
            <div className="absolute top-0 left-20 bottom-0 items-center justify-center w-72 bg-gray-900 bg-opacity-75 hidden lg:flex">
              <p className="text-white text-2xl font-playfair font-bold">Ponyo</p>
              <div className="absolute bottom-20 ml-5 mr-5 text-center">
              <p className="text-white font-playfair font-light italic hidden xl:block">
                "A five-year-old boy develops a relationship with Ponyo,
                a young goldfish princess who longs to become a human after falling in love with him."
              </p>
            </div>
            </div>
          </div>
        </swiper-slide>
      </swiper-container>
    </div>
  )
}

export default Carousel
