import React from 'react'; 
import SentimentSearch from '../../api/SentimentSearch.js'
import {Grid, Card, Stack, CardHeader, CardContent} from '@mui/material'; 
import { makeStyles } from '@mui/styles';

const useStyles = makeStyles({
 cardSearch: {
    textAlign: "center",
    width: "100%",
  }, 
  cardTitle : {
    padding: "1em",
  }, 
  
}); 

const ReviewSearchMenu = ({fetchInput}) => {  

  const classes = useStyles();
    return (
        <Card className={classes.cardSearch}>
          <CardHeader className={classes.cardTitle} title="Advanced Review Search"/>
          <CardContent> 
            <Stack spacing={2}>
            <SentimentSearch fetch={fetchInput} />
            </Stack> 
          </CardContent>
        </Card>
    )
};

export default ReviewSearchMenu; 