import React, { useState } from 'react';
// import Navigation from './Navigation';
// import Footer from './Footer';
import SearchBox from './SearchBox';
import BudgetTiles from './BudgetTiles';

const HomePage = () => {
  const [selectedProduct, setSelectedProduct] = useState(null);

  const handleProductSelect = (product) => {
    setSelectedProduct(product);
    // Redirect to the product details page with pre-filled data
  };

  return (
    <div>
      {/* <Navigation /> */}
      <div className="container py-4">
        <h2 className="text-center mb-5">Air Conditioner Product Search</h2>
        <div className="row">
          <div className="col-md-6">
            <SearchBox onSelect={handleProductSelect} />
          </div>
          <div className="col-md-6">
            <div className="bg-white rounded p-4">
              <h3 className="text-center mb-4">Monthly Bill Budget</h3>
              <BudgetTiles />
            </div>
          </div>
        </div>
      </div>
      {/* <Footer /> */}
    </div>
  );
};

export default HomePage;
