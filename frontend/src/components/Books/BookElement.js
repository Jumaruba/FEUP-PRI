import React from 'react';
import {Card, CardContent, CardMedia, Typography, Box} from '@mui/material'; 
import {makeStyles} from '@mui/styles'; 
import { useNavigate } from "react-router-dom";

const useStyles = makeStyles({
    title: {
        fontWeight: "bold", 
        marginBottom: "0.5em",
    },
    card : {
        display: "flex",
        marginTop: "1em !important", 
        width: "100%"
    }, 
    verticalFlex: {
        display: "flex", 
        flexDirection: "column",
    },
    cardContent : {
        flex: "1 0 auto"
    },
    image : {
        width: 151
    },
    propertyName: {
        fontWeight: 'bold'
    }
}); 
const BookElement = ({element}) => { 
    const navigate = useNavigate();

    const properties = {
        "Rating": element.average_rating,
        "Publisher": element.publisher, 
        "Pages": element.num_pages,
        "Authors": element.authors,
        "Genres": element.genres.replaceAll(";", "; "),
    }

    const handleClick = () => {
        navigate('/book?id=' + element.id);
    }

    const classes = useStyles();
    return (
        <Card className={classes.card} elevation={3} onClick={handleClick}> 
            <CardMedia 
                component='img' 
                image={element.image_url} 
                alt="{element.title}"
                className={classes.image}
            />
            <Box className={classes.verticalFlex}> 
                <CardContent>  
                    <Typography component="h3" variant="h5" className={classes.title}> 
                        {element.title}
                    </Typography>  

                    {Object.keys(properties).map(propertyName => (
                        <Typography component="div" variant="span" key={propertyName}>
                            <span className={classes.propertyName} >{propertyName}: </span> 
                            <span>{properties[propertyName]}</span>
                        </Typography> 
                    ))}
                </CardContent> 
            </Box> 
        </Card> 
    )   
}

export default BookElement; 