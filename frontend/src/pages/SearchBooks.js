import React from 'react';
import {Grid, Box, Typography} from '@mui/material';
import { makeStyles } from '@mui/styles';
import Listing from '../components/Listing';
import BookElement from '../components/Books/BookElement';
import SearchMenu from '../components/Books/BookSearchMenu';

const useStyles = makeStyles({ 
  boxFlex : {
    marginTop: "2em",
    display: "flex",
    flexDirection: "column",
    alignItems: "center"
  }, 
  grid: {
    width: "100%",
  },
  emptyBooks: {
    textAlign: "center",
    marginTop: "2em",
  }
}); 

 

const SearchPage = () => { 
  const classes = useStyles(); 
  const [appState, setAppState] = React.useState({books: null}); 

 const fetchBooks = (apiURL) => {
    fetch(apiURL, {mode:'cors'})
      .then((res) => res.json())
      .then((books) => {
        setAppState({ books: books['response']['docs']});
      });
  }

  /**
   * This function decides if a list of books must be show or a message alerting that the list is empty.
   * @returns Typography element or Listing element. 
   */
  const listBooks = () => {
    if (!appState.books || appState.books === 0) return (
      <Typography className={classes.emptyBooks}>Sorry, no books to show...</Typography>
    ); 
    return (<Listing title="Books" list={appState.books} SearchElement={BookElement}/ > );
  }

  return (
      <Box className={classes.boxFlex}>
        <SearchMenu fetchBooks={fetchBooks}/> 
        <Grid className={classes.grid}> 
          {listBooks()}
        </Grid>
    </Box>
  );
}

export default SearchPage;