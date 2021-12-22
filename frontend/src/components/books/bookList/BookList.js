import React from 'react';

const BookList = (props) => {
  const { books } = props;
  if (!books || books.length === 0) return <p>No books, sorry</p>;
  return (
    <ul>
      <h2 className='list-head'>Book List</h2>
      {
      books.map((book) => {
        return (
          <li key={book.id} className='list'>
            <img src={book.image_url} alt="{book.title}" />
            <span className='book-text'>{book.title} </span>
          </li>
        );
      })}
    </ul>
  );
};

export default BookList;