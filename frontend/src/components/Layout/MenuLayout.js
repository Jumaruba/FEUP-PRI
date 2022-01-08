import React from 'react'; 
import {Card, CardHeader, CardContent} from '@mui/material'; 
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

const MenuLayout = (props) => {  
  const classes = useStyles();
    return (
        <Card className={classes.cardSearch}>
          <CardHeader className={classes.cardTitle} title={props.title}/>
          <CardContent> 
            {props.children}
          </CardContent>
        </Card>
    )
};

export default MenuLayout; 