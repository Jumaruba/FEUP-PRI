import React from 'react';
import SearchLayout from '../components/Layout/SearchLayout';
import ReviewElement from '../components/searchElements/ReviewElement';
import Menu from '../components/common/Menu';
import { fetchInput } from '../api/Search';
import { badSentimentQuery, goodSentimentQuery } from '../api/Queries';


const ReviewSearch = () => {
    const [appState, setAppState] = React.useState({ searchResult: null, searchOption: "0", userInput: "" });

    const searchOptions = [
        {
            text: "Bad Review Search", 
            searchAPI: badSentimentQuery
        },
        {
            text: "Good Review Search", 
            searchAPI: goodSentimentQuery 
        }
    ];

    return (
        <SearchLayout
            SearchElement={ReviewElement}
            searchResult={appState.searchResult}
            noResultMessage="No reviews to show..."
        >
            <Menu
                title="Advanced Review Search"
                onSearchSubmit={fetchInput}
                setAppState={setAppState} 
                appState={appState}
                searchOptions={searchOptions}
            >
            </Menu>
        </SearchLayout>
    );


}

export default ReviewSearch; 