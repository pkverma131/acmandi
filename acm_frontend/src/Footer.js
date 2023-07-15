import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-light py-4 text-center">
      <div className="container">
        <p>&copy; {new Date().getFullYear()} ACMandi. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
