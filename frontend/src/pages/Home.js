import React from 'react';
import { makeStyles } from '@mui/styles';

// Main Components
import AppHeader from '../components/AppHeader';
import Footer from '../components/Footer';
import SearchBooksPage from './SearchBooks';
import SearchReviewsPage from './SearchReviews';

const Home = () => {

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
    <React.Fragment>
      <AppHeader handleBooksView={handleBooksView} handleReviewsView={handleReviewsView} />

      {booksView.active && <SearchBooksPage />}
      {reviewsView.active && <SearchReviewsPage />}

      <Footer />
    </React.Fragment>
  );
}
export default Home;
