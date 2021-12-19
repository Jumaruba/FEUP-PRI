import React from 'react';
const List = (props) => {
  const { repos } = props;
  if (!repos || repos.length === 0) return <p>No repos, sorry</p>;
  return (
    <ul>
      <h2 className='list-head'>Book List</h2>
      {
      repos.map((repo) => {
        return (
          <li key={repo.book_id} className='list'>
            <img src={repo.image_url} alt="{repo.title}" />
            <span className='repo-text'>{repo.title} </span>
            
          </li>
        );
      })}
    </ul>
  );
};
export default List;