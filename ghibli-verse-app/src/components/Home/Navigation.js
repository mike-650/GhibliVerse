import { Link } from 'react-router-dom'
import image from './images/logo.png'

function NavigationBar() {
  return (
    <>
      <div className='flex items-center space-x-4 bg-gray-800 p-3 sticky top-0 z-10'>
        <img
          src={image}
          alt="Home page logo"
          className='rounded-full h-14 w-14 ml-7'
        />
        <Link to={'/'} className='text-2xl  text-white font-semi font-playfair'>GhibliVerse</Link>
        <nav className='mt-1'>
          <ul className='flex'>
            <li className='mx-10 text-white font-playfair text-lg'><a href="films">Films</a></li>
            <li className='text-white font-playfair text-lg'><a href="quizzes">Quizzes</a></li>
          </ul>
        </nav>
      </div>
    </>
  )
}


export default NavigationBar
