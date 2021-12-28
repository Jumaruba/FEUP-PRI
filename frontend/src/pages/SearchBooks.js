import React from 'react';
import {Grid, Box } from '@mui/material';
import { makeStyles } from '@mui/styles';
import Listing from '../components/Listing';
import BookElement from '../components/Books/BookElement';
import SearchMenu from '../components/Books/BookSearchMenu';

const useStyles = makeStyles({ 
  boxFlex : {
    marginTop: "2em",
    display: "flex"
  }
});

const SearchPage = () => {
  const classes = useStyles(); 
  const [appState, setAppState] = React.useState({loading: false, books: null});

const fetchBooks = (apiURL) => {
    fetch(apiURL, {mode:'cors'})
      .then((res) => res.json())
      .then((books) => {
        setAppState({ loading: false, books: books['response']['docs']});
      });
  }

  return (
      <Box className={classes.boxFlex}>
        <SearchMenu fetchBooks={fetchBooks}/>
        <Grid item xs={9}>
          <Listing title="Books" list={appState.books} SearchElement={BookElement} />
        </Grid>
    </Box>
  );
}

export default SearchPage;