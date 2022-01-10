import { createTheme } from '@mui/material/styles';


const theme = createTheme({
    palette: {
        primary: {
            main: "#0071e3"
        },
        secondary: {
            main: "#212121"
        }
    }, 
    status: {
        danger:  "orange"
    },
});

theme.palette = {
    ...theme.palette,
} 

export default theme;