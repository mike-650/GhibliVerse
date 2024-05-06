import { Route, Routes, BrowserRouter } from 'react-router-dom';

import Home from './components/Home/Home';
import SingleFilm from './components/Films/SingleFilm';
import AllFilms from './components/Films/AllFilms';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/film/:id' element={<SingleFilm/>} />
        <Route path='/films' element={<AllFilms/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
