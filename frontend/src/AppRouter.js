import React from "react"; 
import {
    BrowserRouter, 
    Routes, 
    Route
} from "react-router-dom"; 

import PageLayout from './components/Layout/PageLayout'; 
import BookPage from './pages/BookPage'; 
import SearchBooks from './pages/SearchBooks'; 
import SearchReviews from './pages/SearchReviews';

const AppRouter = () => (
    <BrowserRouter>
        <Routes>  
            <Route 
                exact 
                path="/"
                key="/"
                element={
                    <PageLayout key="/">
                        <SearchBooks/>
                    </PageLayout>
                }
            /> 
            <Route 
                exact 
                path="/reviews"
                key="/reviews"
                element={
                    <PageLayout key="/reviews">
                        <SearchReviews/>
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