const express = require('express');
const router = express.Router();
const { getConnection } = require('../../shared/db');
const sql = require('mssql/msnodesqlv8');


router.post('/users/register', getConnection, async (req, res) => {
    const { username, password, address, contactDetails } = req.body;
    try {
        await req.pool.request()
            .input('username', req.sql.VarChar, username)
            .input('password', req.sql.VarChar, password)
            .input('address', req.sql.VarChar, address)
            .input('contactDetails', req.sql.VarChar, contactDetails)
            .query(
            'INSERT INTO BookSelling.Users (username, password, address, contactDetails) VALUES (@username, @password, @address, @contactDetails)'
        );
        res.status(201).send(`User Registered for username:${username}:`);
    } catch (err) {
        console.error(err);
        res.status(500).send(`Error registering user for :${username}:`);
    }
});

router.post('/users/login', getConnection, async (req, res) => {
    const { username, password } = req.body;
    try {
        const result = await req.pool.request()
            .input('username', req.sql.VarChar, username)
            .input('password', req.sql.VarChar, password)
            .query('SELECT * FROM BookSelling.Users WHERE username = @username AND password = @password');
        if (result.recordset && result.recordset.length > 0) {
            res.json({ message: `Login Successful for :${username}:`, user: result.recordset[0] });
        } else {
            res.status(401).send(`Login Failed for :${username}:`);
        }
    } catch (err) {
        console.error(err);
        res.status(500).send(`Error during login for :${username}:`);
    }
});

module.exports = router;