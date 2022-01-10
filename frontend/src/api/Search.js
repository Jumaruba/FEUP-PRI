

export const fetchInput = (appState, setAppState, searchOptions) => {
    console.log(appState);
    const apiURL = searchOptions[appState.searchOption].searchAPI(appState.userInput) 
    fetch(apiURL, { mode: 'cors' })
        .then((res) => res.json())
        .then((resJson) => {
            setAppState({ 
                ...appState,
                searchResult: resJson['response']['docs']
            });
        });
}

