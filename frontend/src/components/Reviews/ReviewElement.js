import React from 'react';

const ReviewElement = ({element}) => {
    return (
         <li key={element.review_id} className='list'>
            <span>{element.title} </span>
            <p>{element.review_text}</p>
          </li>
    )
}

export default ReviewElement; 