import { makeStyles } from "@mui/material";
import React from "react";
import Header from "../AppHeader";
import Footer from "../Footer"; 
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