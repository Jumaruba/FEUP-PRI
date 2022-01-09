

export const fetchInput = (appState, setAppState, searchOptions) => {
    const apiURL = searchOptions[appState.searchOption].searchAPI(appState.userInput)
    fetch(apiURL, { mode: 'cors' })
        .then((res) => res.json())
        .then((resJson) => {
            setAppState({
                userInput: appState.userInput,
                searchOption: appState.searchOption,
                searchResult: resJson['response']['docs']
            });
        });
}

