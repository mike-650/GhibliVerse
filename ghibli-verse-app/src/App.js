import { Route, Routes, BrowserRouter } from 'react-router-dom';

import NavigationBar from './components/Home/Navigation';
import Home from './components/Home/Home';
import SingleFilm from './components/Films/SingleFilm';
import AllFilms from './components/Films/AllFilms';

function App() {
  return (
    <BrowserRouter>
      <NavigationBar />
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/film/:id' element={<SingleFilm/>} />
        <Route path='/films' element={<AllFilms/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
