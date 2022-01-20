import React from 'react';
import {Button, Box} from '@mui/material';
import {makeStyles} from '@mui/styles';
import {useNavigate, useSearchParams} from "react-router-dom";

import BookInfo from '../components/Books/BookInfo.js';

const useStyles = makeStyles({ 
  boxFlex : {
    marginTop: "2em",
    display: "flex"
  }
});

const BookPage = () => {
  const navigate = useNavigate();
  const [bookInfo, setBookInfo] = React.useState({ loading: true, book: null});

  const [searchParams, setSearchParams] = useSearchParams();
  const url = 'http://localhost:9000/solr/books/get?id=' + searchParams.get('id');

  React.useEffect(() => {
    setBookInfo({ loading: true });
    fetch(url, {mode:'cors'})
        .then((res) => res.json())
        .then((bookInfo) => {
            setBookInfo({ loading: false, book: bookInfo['doc'] });
      });
  }, [setBookInfo]);

  // TODO: add loading
  return (
    <>
        <BookInfo info={bookInfo}></BookInfo>
        <Box textAlign='center'>
          <Button style={{minWidth: '300px'}} variant="outlined" title="Go Back" onClick={() => navigate(-1)}>
              Go back
          </Button>
        </Box>
    </>
  );
}

export default BookPage;