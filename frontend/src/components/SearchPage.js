import React from 'react';

const SearchPage = (props) => {
    const [input, setInput] = useState("")
    const [bookList, setBookList] = useState({loading: false, books: null});
  
    const FetchBooks = (input) => {
  
      const apiUrl = BuildQuery(input);
      fetch(apiUrl, {mode:'cors'})
        .then((res) => res.json())
        .then((repos) => {
          setAppState({ loading: false, repos: repos['response']['docs'] });
        });
    }
  
    const UpdateInput = (json_response) => {
      setInput(json_response.target.value);
      console.log(json_response.target.value);
      console.log(input);
      console.log("-");
      FetchBooks(json_response.target.value);
    }
  
    useEffect( () => {FetchBooks('romantic')}, []);
  
    return (
      <div className='App'>
        <div className='container'>
          <h1>Best Books Ever!</h1>
        </div>
        <div className='container'>
          <input placeholder="Enter Post Title" input={input} onChange={UpdateInput} />
        </div>
  
        <div className='repo-container'>
          <ListLoading isLoading={appState.loading} repos={appState.repos} />
        </div>
        <footer>
          <div className='footer'>
            Goodreads Advanced Book Search
          </div>
        </footer>
      </div>
    );
  }
  export default SearchBar;