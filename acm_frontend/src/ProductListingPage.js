// ProductListingPage.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import ProductCard from './ProductCard';

function ProductListingPage() {
  const { monthlyBillRange } = useParams();
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch products based on the monthlyBillRange
    // Set the product data in the state
  }, [monthlyBillRange]);

  return (
    <div>
      <h2>Product Listing</h2>
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}

export default ProductListingPage;
