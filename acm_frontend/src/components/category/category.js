import React from 'react';
import Tile from '../tile';

const Category = ({ title, tiles }) => {
  return (
    <div className="category">
      <h2>{title}</h2>
      <div className="tile-container">
        {tiles.map((tile, index) => (
          <Tile key={index} title={tile.title} image={tile.image} />
        ))}
      </div>
    </div>
  );
};

export default Category;
