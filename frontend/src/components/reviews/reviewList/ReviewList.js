import React from 'react';

const ReviewList = (props) => {
  const { reviews } = props;
  if (!reviews || reviews.length === 0) return <p>No reviews, sorry</p>;
  return (
    <ul>
      <h2 className='list-head'>review List</h2>
      {
      reviews.map((review) => {
        return (
          <li key={review.review_id} className='list'>
            <span className='review-text'>{review.title} </span>
            <p>{review.review_text}</p>
          </li>
        );
      })}
    </ul>
  );
};

export default ReviewList;