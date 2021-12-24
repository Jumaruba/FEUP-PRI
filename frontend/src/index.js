import React from 'react';
import ReactDOM from 'react-dom';
import AppTheme from './AppTheme';  
import AppRouter from './AppRouter';
import { ThemeProvider } from '@mui/material/styles';
import './style.css'; 

ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider theme={AppTheme}>
      <AppRouter/> 
    </ThemeProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

