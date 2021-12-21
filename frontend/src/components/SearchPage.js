import React, { useEffect, useState } from 'react';

import List from './search_page/List';
import WithListLoading from './search_page/WithListLoading';
import BuildQuery from './search_page/BuildQuery';

const SearchPage = (props) => {
  // Hooks
  const ListLoading = WithListLoading(List);
  const [appState, setAppState] = useState({loading: false, books: null});

  const fetchBooks = (input) => {
    const apiUrl = BuildQuery(input);
    fetch(apiUrl, {mode:'cors'})
      .then((res) => res.json())
      .then((books) => {
        setAppState({ loading: false, books: books['response']['docs'] });
      });
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
        <ListLoading isLoading={appState.loading} books={appState.books} />
      </div>
    </>
  );
}

  export default SearchPage;