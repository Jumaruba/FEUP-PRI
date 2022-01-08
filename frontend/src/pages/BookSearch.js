import React from 'react';
import { Stack } from '@mui/material' 
import PageSearch from '../components/Layout/PageSearch'; 
import BookSearchMenu from '../components/Books/BookSearchMenu'; 
import BookElement from '../components/Books/BookElement';
import ThematicSearch from '../api/ThematicSearch';
import MenuLayout from '../components/Layout/MenuLayout';

const BookSearch = () => { 
  const [appState, setAppState] = React.useState({searchResult: null});   

  const fetchInput = (apiURL) => {
      fetch(apiURL, {mode:'cors'})
        .then((res) => res.json())
        .then((resJson) => {
          setAppState({searchResult: resJson['response']['docs']});
        });
    }

    return (
        <PageSearch
            SearchMenuElement={BookSearchMenu}
            SearchElement={BookElement}
            searchResult={appState.searchResult}
            noResultMessage="No books to show..."
        > 
            <MenuLayout title="Advanced Book Search"> 
                <Stack spacing={2}>
                    <ThematicSearch fetch={fetchInput}/>
                </Stack>  
            </MenuLayout>
        </PageSearch> 
    );


}

export default BookSearch; 