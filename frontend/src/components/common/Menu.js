import React from 'react';
import { Card, CardHeader, CardContent, Stack, TextField, Button, FormControl, FormLabel, RadioGroup, FormControlLabel, Radio } from '@mui/material';
import { makeStyles } from '@mui/styles';
import SearchIcon from '@mui/icons-material/Search';

const useStyles = makeStyles({
  cardSearch: {
    textAlign: "center",
    width: "100%",
  },
  cardTitle: {
    padding: "1em",
  },
  searchButton: {
    marginTop: "1em",
    width: "300px !important",
    alignSelf: "center"
  },
  radio: {
    marginTop: "1em",
  }

});

const Menu = ({ title, onSearchSubmit, setAppState, appState, searchOptions }) => {
  const classes = useStyles();

  /**
   * Displays all the radio buttons and updates the state whe they are changed. 
   * @returns Structure with radio buttons. 
   */
  const buildRadioButtons = () => {
    return (<FormControl component="fieldset" className={classes.radio}>
      <FormLabel component="legend">Search Options</FormLabel>
      <RadioGroup row aria-label="search-options" name="row-radio-buttons-group">
        {Object.keys(searchOptions).map(key => buildRadioButton(key))}
      </RadioGroup>
    </FormControl>);
  }

  /**
   * Displays one single radion button.
   * @param {String} key 
   */
  const buildRadioButton = (key) => {
    return (
      <FormControlLabel
        value={key}
        control={<Radio />}
        label={searchOptions[key].text}
        key={key}
        onChange={(event) => setAppState({
          ...appState,
          searchOption: event.target.value,
        })}
      />
    )
  }
  /**
   * This function builds the search button and submit the search on click. 
   * @returns Structure with button object. 
   */
  const buildButtonSearch = () => {
    return (
      <Button
        size="large"
        variant="outlined"
        className={classes.searchButton}
        onClick={() => { onSearchSubmit(appState, setAppState, searchOptions) }}>
        Search
        <SearchIcon />
      </Button>
    );
  }

  /**
   * This function updates the user input in the application state.
   * @returns The structure with the text field. 
   */
  const buildTextField = () => {
    return (
      <TextField
        label="What are you searching for?"
        variant="outlined"
        onChange={(event) => {
          setAppState({
            ...appState,
            userInput: event.target.value,
          })
        }}
      />
    );
  }

  return (
    <Card className={classes.cardSearch}>
      <CardHeader className={classes.cardTitle} title={title} />
      <CardContent>
        <Stack>
          {buildTextField()}
          {buildRadioButtons()}
          {buildButtonSearch()}
        </Stack>
      </CardContent>
    </Card>
  )
};

export default Menu; 