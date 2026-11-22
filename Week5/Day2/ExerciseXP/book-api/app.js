const express = require("express")
const app = express()

app.use(express.json())

const data = [
    {
        id: 1,
        title: "Book 1",
        author: "Author 1",
        year: 2020
    },
    {
        id: 2,
        title: "Book 2",
        author: "Author 2",
        year: 2021
    },
    {
        id: 3,
        title: "Book 3",
        author: "Author 3",
        year: 2022
    },
    {
        id: 4,
        title: "Book 4",
        author: "Author 4",
        year: 2023
    }
]

app.listen(5000, () => {console.log("Server is running on port 5000")})

app.get("/api/books", (req, res) => {
    res.json(data)
})
app.get("/api/books/:id", (req, res) => {
    const bookId = Number(req.params.id)
    const book  = data.find(b => b.id === bookId)
    if (!book) {
        return res.status(404).json({ message: "Book not found" })
    }
    res.status(200).json(book)
})
app.post("/api/books", (req, res) => {
    const { title, author, year } = req.body
    if (!title || !author || !year) {
        return res.status(400).json({ message: "All fields are required" })
    }
    const newBook = {
        id: data.length + 1,
        title,  
        author,
        year
    }
    data.push(newBook)
    res.status(201).json(newBook)
})
