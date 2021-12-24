import React from 'react';
import BookElement from './Books/BookElement';
import {Typography} from '@mui/material'; 


const Listing = ({SearchElement, list}) => {

  if (!list|| list.length === 0) return (
      <p>No books, sorry</p> 
    );

  return (
    <React.Fragment>
      {list.map((listElement) => <SearchElement element={listElement}/>)}
    </React.Fragment>
  );
};

export default Listing;