import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Stack from '@mui/material/Stack';
import Grid from '@mui/material/Grid';

import BookList from './bookList/BookList';
import BookLoading from './bookList/BookLoading';

import ThematicSearch from './search/ThematicSearch';

var cardSearchStyle = {
  textAlign: 'center',
  marginLeft: 'auto',
  marginRight: 'auto',
  display: 'block',
  width: '80%',
  height: '30vw'
}

var cardBookStyle = {
  display: 'block',
  width: '90%',
  minHeight: '45vw',
}

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
    <Box sx={{ mt: 2 }}>
      <Grid container >
        <Grid item xs={3}>
          <Card style={cardSearchStyle} variant="outlined">
            <h2>Advanced Book Search</h2>

            <Stack spacing={2}>
              <ThematicSearch fetch={fetchBooks} />
            </Stack>
          </Card>
        </Grid>

        <Grid item xs={9}>
          <Card style={cardBookStyle} variant="outlined">
            <BookListLoading isLoading={appState.loading} books={appState.books} />
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
}

export default SearchPage;