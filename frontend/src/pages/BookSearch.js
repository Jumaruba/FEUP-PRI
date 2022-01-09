import React from 'react';
import SearchLayout from '../components/Layout/SearchLayout';
import Menu from '../components/common/Menu'; 
import { fetchInput } from '../api/Search';
import BookElement from '../components/searchElements/BookElement';

const BookSearch = () => {
    const [appState, setAppState] = React.useState({ searchResult: null });


    const searchOptions = {
        1: {
            text: "General Search", 
            value: ""
        }, 
        2: {
            text: "Named Entity Search",
            value: ""
        },
        3: {
            text: "Scientific book",
            value: ""
        }, 
        4: {
            text: "Authors", 
            value: ""
        }
    }

    return (
        <SearchLayout
            SearchElement={BookElement}
            searchResult={appState.searchResult}
            noResultMessage="No books to show..."
        >
            <Menu
                title="Advanced Book Search"
                onSearchSubmit={fetchInput}
                setAppState={setAppState} 
                appState={appState}
                searchOptions={searchOptions}
            >
            </Menu>
        </SearchLayout>
    );

}

export default BookSearch; 