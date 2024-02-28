import { Route, Routes, BrowserRouter } from 'react-router-dom';

import Home from './components/Home/Home';
import SingleFilm from './components/Films/SingleFilm';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/film/:id' element={<SingleFilm/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
