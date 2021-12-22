import React from 'react';
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
      <Grid container sx={{ mt: 2 }}>
        <Grid container xs={3}>
          <Card style={cardSearchStyle} variant="outlined">
            <h2>Advanced Review Search</h2>

            <Stack spacing={2}>
              <SentimentSearch fetch={fetchReviews} />
            </Stack>
          </Card>
        </Grid>

        <Grid container xs={9}>
          <Card style={cardReviewStyle} variant="outlined">
            <ReviewListLoading isLoading={reviewState.loading} reviews={reviewState.reviews} />
          </Card>
        </Grid>
      </Grid>
  );
}

  export default SearchPage;