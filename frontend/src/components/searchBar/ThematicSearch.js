import React from 'react';
import TextField from '@mui/material/TextField';

import BuildThematicSearchQuery from '../BuildQuery';

const ThematicSearch = (props) => {
    const updateInput = (json_response) => {
      const apiURL = BuildThematicSearchQuery(json_response.target.value);
      props.fetch(apiURL);
    }

    return (
      <div className='thematic-search'>
          <TextField id="thematic-search-field" label="Thematic Search" variant="outlined" onChange={updateInput} />
      </div>
    );
}

export default ThematicSearch;