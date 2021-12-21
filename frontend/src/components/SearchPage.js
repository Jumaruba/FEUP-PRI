import React, { useEffect, useState } from 'react';

import BookList from './search_page/BookList';
import BookLoading from './search_page/BookLoading';

import BuildQuery from './BuildQuery';

const SearchPage = () => {
  // Hooks
  const BookListLoading = BookLoading(BookList);
  const [appState, setAppState] = useState({loading: false, books: null});

  const fetchBooks = (input) => {
    if(input !== '' && input !== ' ') {
      const apiUrl = BuildQuery(input);
      fetch(apiUrl, {mode:'cors'})
        .then((res) => res.json())
        .then((books) => {
          setAppState({ loading: false, books: books['response']['docs']});
        });
      }
  }

  const updateInput = (json_response) => {
    fetchBooks(json_response.target.value);
  }

  useEffect( () => {fetchBooks('romantic')}, []);

  return (
    <>
      <div className='container'>
        <input placeholder="Enter Post Title" onChange={updateInput} />
      </div>

      <div className='book-container'>
        <BookListLoading isLoading={appState.loading} books={appState.books} />
      </div>
    </>
  );
}

  export default SearchPage;