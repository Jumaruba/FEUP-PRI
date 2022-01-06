import React from 'react';
import { Box, Card, Stack, Grid, Checkbox} from '@mui/material';

import SentimentSearch from '../api/SentimentSearch';
import ReviewElement from '../components/Reviews/ReviewElement';
import Listing from '../components/Listing';

var cardSearchStyle = {
  textAlign: 'center',
  marginLeft: 'auto',
  marginRight: 'auto',
  display: 'block',
  width: '80%',
  height: '30vw'
}

var cardReviewStyle = {
  display: 'block',
  width: '90%',
  minHeight: '45vw',
}

const SearchPage = () => {
  const [reviewState, setReviewState] = React.useState({loading: false, reviews: null});

  const fetchReviews = (apiURL) => {
    fetch(apiURL, {mode:'cors'})
      .then((res) => res.json())
      .then((reviews) => {
        setReviewState({ loading: false, reviews: reviews['response']['docs']});
      });
  }

  return (
    <Box sx={{ mt: 2 }}>
      <Grid container >
        <Grid item xs={3}>
          <Card style={cardSearchStyle} variant="outlined">
            <h2>Advanced Review Search</h2>
            <Stack spacing={2}>
              <Checkbox/>
              <SentimentSearch fetch={fetchReviews} />
            </Stack>
          </Card>
        </Grid>

        <Grid item xs={9}>
          <Card style={cardReviewStyle} variant="outlined"> 
            <Listing title="Reviews" list={reviewState.reviews} SearchElement={ReviewElement} />
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
}

  export default SearchPage;