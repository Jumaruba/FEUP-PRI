import React from 'react';

const BookElement = ({element}) => {
    return (
        <li key={element.id} className='list'>
            <img src={element.image_url} alt="{element.title}" />
            <span>{element.title}</span>
          </li>
    )
}

export default BookElement; 