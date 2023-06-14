import React from 'react';
import "./App.css";


var path = process.env.PUBLIC_URL;

const Tile = ({ title, description, image }) => {
  return (
    <div className="tile">
      <img src={image} alt={title} />
      <p className="tile-description">{description}</p>
      <h3 className="tile-title">{title}</h3>
    </div>
  );
};

const Category = ({ title, tiles }) => {
  return (
    <div className="category">
      <h2>{title}</h2>
      <div className="tile-container">
        {tiles.map((tile, index) => (
          <Tile key={index} title={tile.title} description={tile.description} image={path +tile.image} />
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
        { title: 'Small Bedroom', description:'120-170 sq.ft.', image:  '/media/tiles/thumbnail/small_bedroom.png' },
        { title: 'Big Bedroom',description:'120-170 sq.ft.',  image: '/media/tiles/thumbnail/big_bedroom.png' },
        { title: 'Living Room', description:'120-170 sq.ft.', image: '/media/tiles/thumbnail/living_room.png' }
      ]
    },
    {
      title: 'Choose Your Type',
      tiles: [
        { title: 'Split AC', description:'120-170 sq.ft.', image: '/media/tiles/thumbnail/split_ac.png' },
        { title: 'Window AC', description:'120-170 sq.ft.', image: '/media/tiles/thumbnail/window_ac.png' },
        { title: 'Portable AC', description:'120-170 sq.ft.', image: '/media/tiles/thumbnail/portable_ac.png' },
        { title: 'Hot and Cold AC', description:'120-170 sq.ft.', image: '/media/tiles/thumbnail/hotncold_ac.png' }
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
