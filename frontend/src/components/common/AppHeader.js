import React from 'react'; 
import {Box, Toolbar, Typography, Button, IconButton, AppBar, MenuItem} from '@mui/material';
import {Link} from 'react-router-dom'; 
import MenuBookIcon from '@mui/icons-material/MenuBook';

const AppHeader = () => {
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
            <MenuBookIcon fontSize="large"/>
          </IconButton>

          <Typography 
            variant="h5" 
            component="div" 
            sx={{ flexGrow: 1 }}
          >
            GoodBook 
          </Typography>

          <MenuItem
            component={Link}
            to={'/'}>
              <Button color="inherit">
                Books
              </Button>
            </MenuItem>

          <MenuItem
            component={Link}
            to={'/reviews'}>
              <Button color="inherit">
                Reviews 
              </Button>
            </MenuItem>
        

        </Toolbar>
      </AppBar>
    </Box>
  );
}

export default AppHeader;