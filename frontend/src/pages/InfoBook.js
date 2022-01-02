import React from 'react';
import {Button} from '@mui/material';
import { makeStyles } from '@mui/styles';
import { useNavigate, useSearchParams } from "react-router-dom";

const useStyles = makeStyles({ 
  boxFlex : {
    marginTop: "2em",
    display: "flex"
  }
});

const InfoBook = () => {
  const navigate = useNavigate();

  const [searchParams, setSearchParams] = useSearchParams();
  const id = searchParams.get('id')
  console.log(id);

  return (
    <>
        <h1> Book Title </h1>
        <Button title="Go Back" onClick={() => navigate(-1)}>
            Go back
        </Button>
    </>
  );
}

export default InfoBook;