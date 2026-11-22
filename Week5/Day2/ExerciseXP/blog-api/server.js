const express = require('express');
const app = express();

app.use(express.json());

const data = [
    {
        id: 1,
        title: 'First Post',
        content: 'This is the content of the first post.'
    },
    {
        id: 2,
        title: 'Second Post',
        content: 'This is the content of the second post.'
    },
    {
        id: 3,
        title: 'Third Post',
        content: 'This is the content of the third post.'
    },
    {
        id: 4,
        title: 'Fourth Post',
        content: 'This is the content of the fourth post.'
    }
];

app.get('/posts', (req, res) => {
    res.json(data);
});
app.get('/posts/:id', (req, res) => {
    const postId = Number(req.params.id)
    const post = data.find(p => p.id === postId);
    if (!post) {
        return res.status(404).json({ error: 'Post not found' });
    }
    res.json(post);
});

app.post('/posts', (req, res) => {
    const { title, content } = req.body;
    const newPost = {
        id: data.length + 1,
        title,
        content
    };
    data.push(newPost);
    res.status(201).json(newPost);
});

app.put('/posts/:id', (req, res) => {
    const postId = Number(req.params.id);
    const postIndex = data.findIndex(p => p.id === postId);
    if (postIndex === -1) {
        return res.status(404).json({ error: 'Post not found' });
    }
    const { title, content } = req.body;
    data[postIndex] = { ...data[postIndex], title, content };
    res.json(data[postIndex]);
}); 

app.delete('/posts/:id', (req, res) => {
    const postId = Number(req.params.id);
    const postIndex = data.findIndex(p => p.id === postId);
    if (postIndex === -1) {
        return res.status(404).json({ error: 'Post not found' });
    }
    data.splice(postIndex, 1);
    res.status(204).send();
});

app.use((req, res) => {
    res.status(404).json({ error: 'Route not found' });
});

app.listen(3000, () => {
    console.log('Serveur démarré sur http://localhost:3000');
});

