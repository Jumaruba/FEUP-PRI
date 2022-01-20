import React from 'react';
import {CardMedia, Box, Grid} from '@mui/material'; 
import {makeStyles} from '@mui/styles'; 


const BookInfo = (props) => {

    if(props.info.loading) return (<p>Nothing</p>);

    let genres
    let date = props.info.book['date'].slice(0, 10);
    return (
      <>
        <Box sx={{ m: 5 }} textAlign='center'>
          <h1> { props.info.book['title'] } </h1>
          <h3> By { props.info.book['authors'] }, published by { props.info.book['publisher'] }</h3>
        </Box>
          <Box justify="center" alignItems="center" sx={{ m: 5 }}> 
            <Grid justify="center" alignItems="center" container spacing={3}>
              <Grid sx={{ ml: 80 }} item xs={6} md={1.4}>
                <CardMedia 
                  component='img' 
                  image={props.info.book['image_url']} 
                  alt="{element.title}"
                />
              </Grid>

              <Grid item xs={6}>
                <p>ISBN = { props.info.book['isbn'] }</p> 
                <p>Total Pages: { props.info.book['num_pages'] }</p>
                <p>Rating: { props.info.book['rating'] } </p>
                <p>Release date: { date }</p>
                <p>Genres: { props.info.book['genres'] }</p>
                
              </Grid>
            </Grid>

            <Box sx={{ m: 5 }}>
            <h2>More about this book: </h2>
            <p>{ props.info.book['description'] }</p>
            
            </Box>
          </Box>
        </>
    );
}

export default BookInfo;