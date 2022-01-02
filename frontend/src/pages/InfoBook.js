import React from 'react';
import { makeStyles } from '@mui/styles';
import BookElement from '../components/Books/BookElement';

const useStyles = makeStyles({ 
  boxFlex : {
    marginTop: "2em",
    display: "flex"
  }
});

const InfoBook = (element) => {
  const classes = useStyles(); 
  const properties = {
    "Rating": element.average_rating,
    "Publisher": element.publisher, 
    "Pages": element.num_pages,
    "Authors": element.authors,
    "Genres": element.genres,
  }

  return (
    <>
        <h1> Book Title </h1>
    </>
  );
}

export default InfoBook;