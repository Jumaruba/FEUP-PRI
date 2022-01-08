import React from 'react';
import { makeStyles } from '@mui/styles';
import { Typography } from '@mui/material'; 

const useStyles = makeStyles({
  emptyResult: {
    textAlign: "center",
    marginTop: "2em",
  }
}) ;
/**
 * This class is responsible for generating the list of the items to be searched. 
 * @param {} SearchElement The list item template to be rendered. 
 * @param {} list The list items containing the information to be used by the Search element to be rendered. 
 * @returns 
 */
const Listing = ({SearchElement, searchResult, noResultMessage}) => {
  const classes = useStyles();

    if (!searchResult || searchResult === 0) return ( 
      <Typography className={classes.emptyResult}>{noResultMessage}</Typography>
    ); 
    return (
      searchResult.map((listElement) => <SearchElement element={listElement} key={listElement.title}/>
    ));

};

export default Listing;