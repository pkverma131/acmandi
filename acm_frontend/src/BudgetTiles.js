import React, { useState } from 'react';
import SearchBox from './SearchBox';
import BudgetTiles from './BudgetTiles';

const HomePage = () => {
  const [selectedProduct, setSelectedProduct] = useState(null);

  const handleProductSelect = (product) => {
    setSelectedProduct(product);
    // Redirect to the product details page with pre-filled data
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="max-w-xl bg-white shadow-lg rounded-lg p-8">
        <h2 className="text-2xl font-bold mb-6">Air Conditioner Product Search</h2>
        <div className="grid grid-cols-2 gap-6">
          <div>
            <SearchBox onSelect={handleProductSelect} />
          </div>
          <div>
            <div className="bg-gray-200 rounded-lg p-4">
              <h3 className="text-lg font-semibold mb-4">Monthly Bill Budget</h3>
              <BudgetTiles />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
