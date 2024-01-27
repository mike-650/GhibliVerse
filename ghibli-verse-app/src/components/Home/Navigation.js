import image from './images/logo.png'

function NavigationBar() {
  return (
    <>
      <div className='flex items-center space-x-4 bg-gray-400 p-3'>
        <img
          src={image}
          alt="Home page logo"
          className='rounded-full h-14 w-14 ml-7'
        />
        <h1 className='text-2xl  text-white font-semi font-playfair'>GhibliVerse</h1>
        <nav>
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
