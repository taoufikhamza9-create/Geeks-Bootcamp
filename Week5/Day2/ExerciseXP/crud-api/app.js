const express = require('express');
const app = express();
const { fetchPosts } = require('./data/dataService');       

// Middleware to parse JSON requests
app.use(express.json());

app.listen(5000, () => {
  console.log('Server is running on port 5000');
});

app.get('/posts', async (req, res) => {
  try {
    const posts = await fetchPosts();   
    res.status(200).json(posts);
    console.log('Posts fetched successfully');
    } catch (error) {  
        res.status(500).json({ error: error.message });
    }
});  
