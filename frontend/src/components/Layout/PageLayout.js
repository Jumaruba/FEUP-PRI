import React from "react";
import Header from "../AppHeader";
import Footer from "../Footer"; 

const PageLayout = ({children}) => (
    <div>
        <Header/>
            {children}
        <Footer/> 
    </div> 
)

export default PageLayout;