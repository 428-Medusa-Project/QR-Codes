import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Redirect from './Redirect';
import RedirectToWiki from './Wiki';

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      
      <Router>
        <Routes>
          <Route path="/" element={<h1>Test Page</h1>} />
          <Route path="/redirect/:to" element={<Redirect />} />
          <Route path="/wiki" element={<RedirectToWiki />} />
          <Route path="*" element={<h1>Page not found</h1>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
