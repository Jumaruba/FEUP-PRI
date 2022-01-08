import React from 'react';
import TextField from '@mui/material/TextField';
import { Box } from '@mui/system';

const ThematicSearch = (props) => {
    const BuildThematicSearchQuery = (search) => {
      const options = {
          "description:" : search,
          "q.op=": "OR",
          "defType=": "edismax",
          "qf=": "description%5E2",
          "ps=": "4",
      }

        let full_query = 'http://localhost:9000/solr/books/select?q=';
      for (let option in options)
          full_query += option + options[option] + '&';

      return full_query + 'wt=json';
    }

    const updateInput = (json_response) => {
      const apiURL = BuildThematicSearchQuery(json_response.target.value);
      props.fetch(apiURL);
    }

    return (
        <TextField id="thematic-search-field" label="Thematic Search" variant="outlined" onChange={updateInput} />
    );
}

export default ThematicSearch;