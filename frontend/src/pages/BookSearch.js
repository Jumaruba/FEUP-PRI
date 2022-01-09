import React from 'react';
import SearchLayout from '../components/Layout/SearchLayout';
import Menu from '../components/common/Menu'; 
import { fetchInput } from '../api/Search';
import BookElement from '../components/searchElements/BookElement';
import { thematicSearch } from '../api/Queries';

const BookSearch = () => {
    const [appState, setAppState] = React.useState({ searchResult: null });

    const searchOptions = [
        {
            text: "General Search",     // Radio name to display 
            searchAPI: ""
        },
        {
            text: "Named Entity Search",
            searchAPI: ""
        },
        {
            text: "Scientific book",
            searchAPI: ""
        }, 
        {
            text: "Authors", 
            searchAPI: ""
        }, 
        {
            text: "Thematic Search",
            searchAPI: thematicSearch
        }
    ]

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