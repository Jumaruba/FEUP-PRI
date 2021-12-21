import React from 'react';

import BuildThematicSearchQuery from '../BuildQuery';

const ThematicSearch = (props) => {
    const updateInput = (json_response) => {
      const apiURL = BuildThematicSearchQuery(json_response.target.value);
      props.fetch(apiURL);
    }

    return (
      <div className='thematic-search'>
          <input placeholder="Enter Post Title" onChange={updateInput} />
      </div>
    );
}

export default ThematicSearch;