import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Stack from '@mui/material/Stack';
import Grid from '@mui/material/Grid';

import ReviewList from './reviewList/ReviewList';
import ReviewLoading from './reviewList/ReviewLoading';
import SentimentSearch from './search/SentimentSearch';

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
  const ReviewListLoading = ReviewLoading(ReviewList);
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
              <SentimentSearch fetch={fetchReviews} />
            </Stack>
          </Card>
        </Grid>

        <Grid item xs={9}>
          <Card style={cardReviewStyle} variant="outlined">
            <ReviewListLoading isLoading={reviewState.loading} reviews={reviewState.reviews} />
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
}

  export default SearchPage;