import React from 'react';
import "./App.css";


var path = process.env.PUBLIC_URL;

const Tile = ({ title, image }) => {
  return (
    <div className="tile">
      <img src={image} alt={title} />
    </div>
  );
};

const Category = ({ title, tiles }) => {
  return (
    <div className="category">
      <h2>{title}</h2>
      <div className="tile-container">
        {tiles.map((tile, index) => (
          <Tile key={index} title={tile.title} image={path +tile.image} />
        ))}
      </div>
    </div>
  );
};


const HomePage = () => {
  const categories = [
    {
      title: 'Size Up Your Room',
      tiles: [
        { title: 'Small Bedroom', image:  '/media/tiles/thumbnail/small_bedroom.png' },
        { title: 'Big Bedroom', image: '/media/tiles/thumbnail/big_bedroom.png' },
        { title: 'Living Room', image: '/media/tiles/thumbnail/living_room.png' }
      ]
    },
    {
      title: 'Choose Your Type',
      tiles: [
        { title: 'Split AC', image: '/media/tiles/thumbnail/split_ac.png' },
        { title: 'Window AC', image: '/media/tiles/thumbnail/window_ac.png' },
        { title: 'Portable AC', image: '/media/tiles/thumbnail/portable_ac.png' },
        { title: 'Hot and Cold AC', image: '/media/tiles/thumbnail/hotncold_ac.png' }
      ]
    }
  ];

  return (
    <div>
      <h1>Best Air Conditioners to cool you down</h1>
      {categories.map((category, index) => (
        <Category key={index} title={category.title} tiles={category.tiles} />
      ))}
    </div>
  );
};

const App = () => {
  return (
    <div>
      <HomePage />
    </div>
  );
};

export default App;
