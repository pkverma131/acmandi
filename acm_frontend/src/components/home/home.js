import React from 'react';
import Category from '..category/category';

const HomePage = () => {
  const categories = [
    {
      title: 'Category 1',
      tiles: [
        { title: 'Tile 1', image: 'path/to/image1.jpg' },
        { title: 'Tile 2', image: 'path/to/image2.jpg' },
        { title: 'Tile 3', image: 'path/to/image3.jpg' }
      ]
    },
    {
      title: 'Category 2',
      tiles: [
        { title: 'Tile 4', image: 'path/to/image4.jpg' },
        { title: 'Tile 5', image: 'path/to/image5.jpg' },
        { title: 'Tile 6', image: 'path/to/image6.jpg' }
      ]
    }
  ];

  return (
    <div>
      <h1>Home Page</h1>
      {categories.map((category, index) => (
        <Category key={index} title={category.title} tiles={category.tiles} />
      ))}
    </div>
  );
};

export default HomePage;
