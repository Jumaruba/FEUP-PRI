import React from 'react';

// Main Components
import AppHeader from './components/AppBar';

import SearchBooksPage from './components/books/SearchBooksPage';
import SearchReviewsPage from './components/reviews/SearchReviewsPage';

// Styles
import './App.css';

const App = () => {
  return (
    <div>
      <AppHeader />

      <SearchBooksPage />
      <SearchReviewsPage />

      <footer>
        <div className='footer'>
          Goodreads Advanced Book Search. Made with ❤️ from G53.
        </div>
      </footer>
    </div>
  );
}
export default App;
