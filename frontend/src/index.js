import React from 'react';
import ReactDOM from 'react-dom';
import Home from './pages/Home'; 
import AppTheme from './AppTheme'; 
import { ThemeProvider } from '@mui/material/styles';
import './style.css'; 

ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider theme={AppTheme}>
      <Home/> 
    </ThemeProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

