import React from "react"; 
import {
    BrowserRouter, 
    Routes, 
    Route
} from "react-router-dom"; 

import PageLayout from './components/Layout/PageLayout.js'; 
import BookPage from './pages/BookPage';  
import BookSearch from './pages/BookSearch'; 
import ReviewSearch from "./pages/ReviewSearch";

const AppRouter = () => (
    <BrowserRouter>
        <Routes>  
            <Route 
                exact 
                path="/"
                key="/"
                element={
                    <PageLayout key="/">
                        <BookSearch/>
                    </PageLayout>
                }
            /> 
            <Route 
                exact 
                path="/reviews"
                key="/reviews"
                element={
                    <PageLayout key="/reviews"> 
                        <ReviewSearch/> 
                    </PageLayout>
                }/>
            <Route 
                replace
                path="/book"
                key="/book"
                element={
                    <PageLayout key="/book">
                        <BookPage />
                    </PageLayout>
                }/>
        </Routes> 
    </BrowserRouter>
);

export default AppRouter;