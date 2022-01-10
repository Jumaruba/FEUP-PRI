import React from "react";
import Header from "../common/AppHeader";
import Footer from "../common/Footer"; 
import { Box } from "@mui/system"; 

const PageLayout = ({children}) => {
    return (
        <div>
            <Header/> 
                <Box sx={{"paddingInline": "5em"}}> 
                    {children} 
                </Box>
            <Footer/> 
        </div> 
    ); 
} 

export default PageLayout;