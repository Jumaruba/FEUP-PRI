import React from 'react'; 

import ThematicSearch from '../../api/ThematicSearch';
import {Grid, Card, Stack, CardHeader, CardContent} from '@mui/material'; 
import { makeStyles } from '@mui/styles';

const useStyles = makeStyles({
 cardSearch: {
    textAlign: "center",
    width: "80%",
  }, 
  cardTitle : {
    padding: "1em",
  }, 
  
}); 

const BookSearchMenu = ({fetchBooks}) => {  

  const classes = useStyles();
    return (
        <Card className={classes.cardSearch}>
          <CardHeader className={classes.cardTitle} title="Advanced Book Search"/>
          <CardContent> 
            <Stack spacing={2}>
            <ThematicSearch fetch={fetchBooks} />
            </Stack> 
          </CardContent>
        </Card>
    )
};

export default BookSearchMenu; 