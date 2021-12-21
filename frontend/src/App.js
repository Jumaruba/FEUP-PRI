import React from 'react';

// Main Components
import SearchPage from './components/SearchPage';

// Styles
import './App.css';

const App = () => {
  return (
    <div className='App'>
      <div className='container'>
        <h1>Best Books Ever!</h1>
      </div>
      
      <SearchPage />

      <footer>
        <div className='footer'>
          Goodreads Advanced Book Search
        </div>
      </footer>
    </div>
  );
}
export default App;
