import React from 'react';

const ReviewLoading = (Component) => {
  return function WihLoadingComponent({ isLoading, ...props }) {
    if (!isLoading) return <Component {...props} />;
    return (
      <p style={{ textAlign: 'center', fontSize: '30px' }}>
        Fetching Reviews
      </p>
    );
  };
}
export default ReviewLoading;