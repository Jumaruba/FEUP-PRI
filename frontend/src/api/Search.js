import React from 'react';
import TextField from '@mui/material/TextField';

const Search = ({buildQuery, label, fetch}) => {
    const updateInput = (userInput) => {
      const apiURL = buildQuery(userInput.target.value);
      fetch(apiURL);
    }

    return (
        <TextField label={label} variant="outlined" onChange={updateInput} />
    );
}

export default Search;