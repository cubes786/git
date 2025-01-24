// backend/routes/books.js
const express = require('express');
const router = express.Router();
const { getConnection } = require('../../shared/db');
const sql = require('mssql/msnodesqlv8');


// Route handler for fetching all books
router.get('/books', getConnection, async (req, res) => {
    try {
        const result = await req.pool.request().query('SELECT id, title, author, isbn, price, imageUrl FROM bookselling.Books');
        res.json(result.recordset);
    } catch (err) {
        console.error('Error fetching all books:', err);
        res.status(500).send('Error fetching books');
    }
});

// Route handler for fetching a specific book by ID
router.get('/books/:id', getConnection, async (req, res) => {
    const bookId = req.params.id;
    try {
        const result = await req.pool.request()
            .input('id', req.sql.Int, bookId)
            .query('SELECT id, title, author, isbn, price, imageUrl FROM bookselling.Books WHERE id = @id');
        if (result.recordset && result.recordset.length > 0) {
            res.json(result.recordset[0]);
        } else {
            res.status(404).send(`Book with id:${bookId} not found`);
        }
    } catch (err) {
        console.error(`Error fetching book with id ${bookId}:`, err);
        res.status(500).send(`Error fetching book with id ${bookId}`);
    }
});


module.exports = router;