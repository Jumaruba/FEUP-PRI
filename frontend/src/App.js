import React from 'react';

// Main Components
import AppBar from './components/AppBar';
import SearchPage from './components/SearchPage';

// Styles
import './App.css';

const App = () => {
  return (
    <div>
      <AppBar />

      <SearchPage />

      <footer>
        <div className='footer'>
          Goodreads Advanced Book Search. Made with ❤️ from G53.
        </div>
      </footer>
    </div>
  );
}
export default App;
