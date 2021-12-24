import React from 'react';
import {Grid, Card, Box } from '@mui/material';
import { makeStyles } from '@mui/styles';
import Listing from '../components/Listing';
import BookElement from '../components/books/BookElement';
import SearchMenu from '../components/books/BookSearchMenu';

const useStyles = makeStyles({
  
  cardBook: {
    display: 'block',
    width: '90%',
    minHeight: '45vw',
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
      <Box sx={{ mt: 2 }}>
        <Grid container >
        <SearchMenu fetchBooks={fetchBooks}/>
        <Grid item xs={9}>
          <Card className={classes.cardBook} variant="outlined">
            <Listing title="Books" list={appState.books} SearchElement={BookElement} />
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
}

export default SearchPage;