import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';


const AppHeader = (props) => {
  const menuOptions =  {
    'Books': props.handleBooksView, 
    'Reviews': props.handleReviewsView
  };

  return (
    <Box>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            sx={{ mr: 2 }}
          >
            <img src='/favicon.ico' alt="Your Book" />
          </IconButton>

          <Typography 
            variant="h5" 
            component="div" 
            sx={{ flexGrow: 1 }}
          >
            GoodBook 
          </Typography>

          {/* Displays the menu options */}
          {Object.keys(menuOptions).map(title => (
            <Button
              key = {title}
              color="inherit" 
              onClick={menuOptions[title]}>
                {title}
              </Button>
          ))}
        </Toolbar>
      </AppBar>
    </Box>
  );
}

export default AppHeader;