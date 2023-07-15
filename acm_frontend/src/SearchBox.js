import React from 'react';

const SearchBox = ({ onSelect }) => {
  const handleSearch = (e) => {
    e.preventDefault();
    const searchValue = e.target.elements.search.value;
    // Perform search or other actions
  };

  return (
    <form onSubmit={handleSearch}>
      <div className="input-group">
        <input
          type="text"
          className="form-control"
          placeholder="Search for air conditioner products..."
          name="search"
        />
        <button type="submit" className="btn btn-primary">Search</button>
      </div>
    </form>
  );
};

export default SearchBox;
