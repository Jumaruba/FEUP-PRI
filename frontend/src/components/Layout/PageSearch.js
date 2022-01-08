import React from 'react';
import {Grid, Box} from '@mui/material';
import { makeStyles } from '@mui/styles';
import Listing from '../Listing';
import MenuLayout from '../Layout/MenuLayout'

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

 

const SearchPage = ({SearchElement, searchResult, noResultMessage, children}) => { 
  const classes = useStyles();  
  return (
      <Box className={classes.boxFlex}>
        <MenuLayout> 
          {children}
        </MenuLayout>
        <Grid className={classes.grid}> 
          <Listing SearchElement={SearchElement} searchResult={searchResult} noResultMessage={noResultMessage}/> 
        </Grid>
    </Box>
  );
}

export default SearchPage;