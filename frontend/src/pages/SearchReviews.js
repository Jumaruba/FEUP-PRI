import React from 'react';
import { Box } from '@mui/material';
import { makeStyles } from '@mui/styles';
import ReviewElement from '../components/Reviews/ReviewElement';
import Listing from '../components/Listing';
import SearchMenu from '../components/Reviews/ReviewsSearchMenu';

const useStyles = makeStyles({ 
  boxFlex : {
    marginTop: "2em",
    display: "flex",
    flexDirection: "column",
    alignItems: "center"
  }, 
});

const SearchPage = () => {
  const classes = useStyles();

  const [appState, setAppState] = React.useState({reviews: null});
  
  // Get the reviews based on the input.
  const fetchReviews = (apiURL) => {
    fetch(apiURL, {mode:'cors'})
      .then((res) => res.json())
      .then((reviews) => {
        setAppState({reviews: reviews['response']['docs']});
      });
  }

  return (
    <Box className={classes.boxFlex}>
      <SearchMenu fetchReviews={fetchReviews} />
      <Listing title="Reviews" list={appState.reviews} SearchElement={ReviewElement} errorMessage="Sorry, no reviews to show."/>
    </Box>
  )}

  export default SearchPage;