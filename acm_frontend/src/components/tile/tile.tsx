import React from 'react';

const Tile = ({ title, image }) => {
  return (
    <div className="tile">
      <img src={image} alt={title} />
      <h3>{title}</h3>
    </div>
  );
};

export default Tile;
