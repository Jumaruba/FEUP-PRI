import React from 'react';
import { Stack } from '@mui/material' 
import SearchLayout from '../components/Layout/SearchLayout'; 
import ReviewElement from '../components/searchElements/ReviewElement';
import SentimentSearch from '../api/SentimentSearch';
import MenuLayout from '../components/Layout/MenuLayout';

const ReviewSearch = () => { 
  const [appState, setAppState] = React.useState({searchResult: null});   

  const fetchInput = (apiURL) => {
      fetch(apiURL, {mode:'cors'})
        .then((res) => res.json())
        .then((resJson) => {
          setAppState({searchResult: resJson['response']['docs']});
        });
    }
    
    return (
        <SearchLayout
            SearchElement={ReviewElement}
            searchResult={appState.searchResult}
            noResultMessage="No reviews to show..."
        > 
            <MenuLayout title="Advanced Review Search"> 
                <Stack spacing={2}>
                    <SentimentSearch fetch={fetchInput} />
                </Stack>  
            </MenuLayout>
        </SearchLayout> 
    );


}

export default ReviewSearch; 