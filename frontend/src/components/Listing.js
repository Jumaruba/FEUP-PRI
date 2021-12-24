import React from 'react';
import BookElement from './books/BookElement';

const Listing = ({SearchElement, list, title}) => {

  if (!list|| list.length === 0) return <p>No books, sorry</p>;

  return (
    <ul>
      <h2 className='list-head'>{title}</h2>
      {list.map((listElement) => <SearchElement element={listElement}/>)}
    </ul>
  );
};

export default Listing;