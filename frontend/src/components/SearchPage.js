import React from 'react';

import BookList from './bookList/BookList';
import BookLoading from './bookList/BookLoading';

import ThematicSearch from './searchBar/ThematicSearch';

const SearchPage = () => {
  const BookListLoading = BookLoading(BookList);
  const [appState, setAppState] = React.useState({loading: false, books: null});

  const fetchBooks = (apiURL) => {
    fetch(apiURL, {mode:'cors'})
      .then((res) => res.json())
      .then((books) => {
        setAppState({ loading: false, books: books['response']['docs']});
      });
  }

  return (
    <>
      <ThematicSearch fetch={fetchBooks} />
      
      <div className='book-container'>
        <BookListLoading isLoading={appState.loading} books={appState.books} />
      </div>
    </>
  );
}

  export default SearchPage;