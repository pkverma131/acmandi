import React from 'react';
import { Container,Row, Col } from 'react-bootstrap';

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


const HomePageContent = () => {
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


const TopNavigation = () => {
  return (
    <nav className="top-navigation">
      <ul className="menu-items">
        <li><a href="/">Home</a></li>
        <li><a href="/about">Explore</a></li>
        <li><a href="/services">Calculate</a></li>
        <li><a href="/contact">Blogs</a></li>
      </ul>
    </nav>
  );
};

const App = () => {
  return (
    <div>
      <Container>
      <TopNavigation></TopNavigation>
      </Container>
      <Container>
        <Row>
          <Col>
          <HomePageContent/>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default App;
