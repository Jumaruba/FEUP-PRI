import React from 'react';

// Main Components
import AppHeader from './components/AppHeader';
import Footer from './components/Footer';

import SearchBooksPage from './components/books/SearchBooksPage';
import SearchReviewsPage from './components/reviews/SearchReviewsPage';

// Styles
import './App.css';

const App = () => {
  const [booksView, setBooksView] = React.useState({active : true});
  const [reviewsView, setReviewsView] = React.useState({active : false});

  const handleBooksView = () => {
      setReviewsView({
        active: false,
      });
      setBooksView({
          active: true,
      });
  }

  const handleReviewsView = () => {
    setReviewsView({
      active: true,
    });

    setBooksView({
        active: false,
    });
}


  return (
    <div>
      <AppHeader handleBooksView={handleBooksView} handleReviewsView={handleReviewsView} />

      {booksView.active && <SearchBooksPage />}
      {reviewsView.active && <SearchReviewsPage />}

      <Footer />
    </div>
  );
}
export default App;
