import React from 'react';
import TextField from '@mui/material/TextField';

const SentimentSearch = (props) => {
    const BuildSentimentQuery = (search) => {
      const options = {
          "q=": "{!q.op=OR df=review_text}" + search,
      }
    
      let full_query = 'http://localhost:9000/solr/reviews/select?';
      for (let option in options)
          full_query += option + options[option] + '&';
      
      console.log(full_query)
      return full_query + 'wt=json';
    }

    const updateInput = (json_response) => {
      const apiURL = BuildSentimentQuery(json_response.target.value);
      props.fetch(apiURL);
    }

    return (
      <div className='sentiment-search'>
          <TextField id="sentiment-search-field" label="Sentiment Search" variant="outlined" onChange={updateInput} />
      </div>
    );
}

export default SentimentSearch;