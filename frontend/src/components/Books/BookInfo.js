import React from 'react';
import {CardMedia, Box, Grid} from '@mui/material'; 
import {makeStyles} from '@mui/styles'; 

const useStyles = makeStyles({

}); 

const BookInfo = (props) => {
    const styles = useStyles();

    if(props.info.loading) return (<p>Nothing</p>);
    return (
        <Box sx={{ m: 4 }}> 
          <Grid container spacing={3}>
            <Grid item>
              <CardMedia 
                component='img' 
                image={props.info.book['image_url']} 
                alt="{element.title}"
                className={styles.image}
              />
            </Grid>
            <Grid item xs={6} md={10}>
              <h1> { props.info.book['title'] } </h1>
              <h2> By { props.info.book['authors'] },  Published by { props.info.book['publisher'] }</h2>
              <p>Rating: { props.info.book['average_rating'] } </p>
              <p>Release date: { props.info.book['date'] }</p>
            </Grid>
          </Grid>


          <h3>More about this book: </h3>
          <p>{ props.info.book['description'] }</p>
          

          <h3>Genres</h3>
          <p>{ props.info.book['genres'] }</p>

          <h3>More Information </h3>
          <p>Id = { props.info.book['isbn'] }</p>
          <p>ISBN13 = { props.info.book['isbn13'] }</p>

          <h3>Book format: </h3>
          <p>Ebook: { props.info.book['is_ebook'] }</p>
          <p>Format: { props.info.book['format'] }</p>
          
          <p>Total_Pages: { props.info.book['num_pages'] }</p>
          <p>Extra_information: { props.info.book['edition_information'] }</p>
        </Box>
    );
}

export default BookInfo;