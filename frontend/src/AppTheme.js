import { createTheme } from '@mui/material/styles';


const theme = createTheme({
    palette: {
        primary: {
            main: "#6D9886"
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