import React from 'react'; 

import ThematicSearch from '../../searches/ThematicSearch';
import {Grid, Card, Stack, CardHeader, CardContent} from '@mui/material'; 
import { makeStyles } from '@mui/styles';

const useStyles = makeStyles({
 cardSearch: {
    textAlign: 'center',
    marginLeft: 'auto',
    marginRight: 'auto',
    display: 'block',
    width: '80%',
    height: '30vw'
  }, 
  cardTitle : {
    padding: "2em",
  }
}); 

const BookSearchMenu = ({fetchBooks}) => {  

  const classes = useStyles();
    return (
        <Grid item xs={3}>
        <Card className={classes.cardSearch} variant="outlined">
          <CardHeader className={classes.cardTitle} title="Advanced Book Search"/>
            
          <CardContent> 
            <Stack spacing={2}>
            <ThematicSearch fetch={fetchBooks} />
            </Stack> 
          </CardContent>
        </Card>
        </Grid>
    )
};

export default BookSearchMenu; 