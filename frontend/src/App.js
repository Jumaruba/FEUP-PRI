import React, { useEffect, useState } from 'react';
import './App.css';
import List from './components/List';
import withListLoading from './components/withListLoading';
function App() {
  const ListLoading = withListLoading(List);
  const [appState, setAppState] = useState({
    loading: false,
    repos: null,
  });

  useEffect(() => {
    setAppState({ loading: true });

    const apiUrl = `http://localhost:80/solr/books_subset_1/select?q=description:romantic%26tragedy&rows=8&wt=json`;
    fetch(apiUrl, {mode:'cors'})
      .then((res) => res.json())
      .then((repos) => {
        console.log(repos['response']['docs']);
        setAppState({ loading: false, repos: repos['response']['docs'] });
      });
  }, [setAppState]);
  return (
    <div className='App'>
      <div className='container'>
        <h1>Best Books Ever!</h1>
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
export default App;
