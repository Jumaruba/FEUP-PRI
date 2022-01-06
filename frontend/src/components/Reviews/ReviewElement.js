import React from 'react';
import {Card, CardContent, CardMedia, Typography, Box, Divider} from '@mui/material'; 
import {makeStyles} from '@mui/styles'; 
import { elementTypeAcceptingRef } from '@mui/utils';

const useStyles = makeStyles({
    title: {
      fontWeight: "bold",
      marginBottom: "0.5em",
    },
    card : {
        display: "flex",
        marginTop: "1em !important",
    }, 
    verticalFlex: {
        display: "flex", 
        flexDirection: "column", 
        width: "100%",
    },
    cardContent : {
        flex: "1 0 auto",
    },
    image : {
        width: 151
    },
    propertyName: {
        fontWeight: 'bold'
    },
    divider: {
      marginTop: "1em", 
      marginBottom: "1em",
      width: "100%",
    }
}); 
const ReviewElement = ({element}) => { 
    const properties = {
        "Date": element.date_added.replace("T", " ").replace("Z", " "),
        "Rating": element.rating, 
        "Authors": element.authors,
        "Genres": element.genres.replaceAll(";", "; "),
    }
    const classes = useStyles();
    return (
        <Card className={classes.card} elevation={3}> 
            <Box className={classes.verticalFlex}> 
                <CardContent>  
                    <Typography component="h3" variant="h5" className={classes.title}> 
                        {element.title}
                    </Typography>  

                    {Object.keys(properties).map(propertyName => (
                        <Typography component="div" variant="span" key={propertyName}>
                            <span className={classes.propertyName}>{propertyName}: </span> 
                            <span>{properties[propertyName]}</span>
                        </Typography> 
                    ))}
                    <Divider className={classes.divider}/> 
                    <Typography component="div" variant="span" key="review">
                      <span className={classes.propertyName} >Review:</span> 
                      <p>{element.review_text}</p>
                    </Typography> 




                </CardContent> 
            </Box> 
        </Card> 
    )   
}

export default ReviewElement; 