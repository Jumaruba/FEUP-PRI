import React from 'react';

/**
 * This class is responsible for generating the list of the items to be searched. 
 * @param {} SearchElement The list item template to be rendered. 
 * @param {} list The list items containing the information to be used by the Search element to be rendered. 
 * @returns 
 */
const Listing = ({SearchElement, list}) => {

  return (
    <>
      {list.map((listElement) => <SearchElement element={listElement} key={listElement.title}/>)}
    </>
  );
};

export default Listing;