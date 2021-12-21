import React from 'react';

const WithListLoading = (Component) => {
  return function WihLoadingComponent({ isLoading, ...props }) {
    if (!isLoading) return <Component {...props} />;
    return (
      <p style={{ textAlign: 'center', fontSize: '30px' }}>
        Fetching Books
      </p>
    );
  };
}
export default WithListLoading;