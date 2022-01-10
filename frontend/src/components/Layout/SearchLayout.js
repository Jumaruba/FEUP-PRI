import React from 'react';
import {Grid, Box} from '@mui/material';
import { makeStyles } from '@mui/styles';
import Listing from '../Listing';

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
}); 

const SearchLayout= ({SearchElement, searchResult, noResultMessage, children}) => { 
  const classes = useStyles();  
  return (
      <Box className={classes.boxFlex}>
        {children}
        <Grid className={classes.grid}> 
          <Listing SearchElement={SearchElement} searchResult={searchResult} noResultMessage={noResultMessage}/> 
        </Grid>
    </Box>
  );
}

export default SearchLayout;