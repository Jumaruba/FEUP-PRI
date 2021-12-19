import logo from './logo.svg';
import './App.css';

function App() {
  fetch('http://localhost/solr/books_subset_1/select?q=description:romantic%26tragedy&rows=8&wt=json', {mode: 'cors'})
  .then(response => response.json())
  .then(data => console.log(data));
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
