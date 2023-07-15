// BlogPage.js
import React, { useEffect, useState } from 'react';
import BlogCard from './BlogCard';

function BlogPage() {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    // Fetch blog posts
    // Set the blog data in the state
  }, []);

  return (
    <div>
      <h2>Blogs</h2>
      {blogs.map((blog) => (
        <BlogCard key={blog.id} blog={blog} />
      ))}
    </div>
  );
}

export default BlogPage;
