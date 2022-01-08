import React from 'react';
import { Stack } from '@mui/material'
import SearchLayout from '../components/Layout/SearchLayout';
import BookElement from '../components/Books/BookElement';
import ThematicSearch from '../api/ThematicSearch';
import MenuLayout from '../components/Layout/MenuLayout';

const BookSearch = () => {
    const [appState, setAppState] = React.useState({ searchResult: null });

    const fetchInput = (apiURL) => {
        fetch(apiURL, { mode: 'cors' })
            .then((res) => res.json())
            .then((resJson) => {
                setAppState({ searchResult: resJson['response']['docs'] });
            });
    }

    return (
        <SearchLayout
            SearchElement={BookElement}
            searchResult={appState.searchResult}
            noResultMessage="No books to show..."
        >
            <MenuLayout title="Advanced Book Search">
                <Stack spacing={2}>
                    <ThematicSearch fetch={fetchInput} />
                </Stack>
            </MenuLayout>
        </SearchLayout>
    );


}

export default BookSearch; 