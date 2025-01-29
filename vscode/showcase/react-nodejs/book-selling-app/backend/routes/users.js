const express = require('express');
const router = express.Router();
const { getConnection } = require('../../shared/db');
const sql = require('mssql/msnodesqlv8');
const jwt = require('jsonwebtoken');
const { authenticateToken } = require('../../shared/auth');


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
            const user = result.recordset[0];
            const accessToken = generateAccessToken({username: user.username, id: user.id});
            res.json({ message: `Login Successful for :${username}:`, user:user, accessToken: accessToken });
        } else {
            res.status(401).send(`Login Failed for :${username}:`);
        }
    } catch (err) {
        console.error(err);
        res.status(500).send(`Error during login for :${username}:`);
    }
});


// Example of a protected route (requires authentication)
router.get('/users/profile', authenticateToken, getConnection, async (req, res) => {
    // req.user is populated from the JWT token by the authenticateToken middleware
    try {
        const result = await req.pool.request()
            .input('username', req.sql.VarChar, req.user.username)
            .query('SELECT * FROM BookSelling.Users WHERE username = @username');
        if (result.recordset.length > 0) {
            res.json({ message: `Profile fetched for :${req.user.username}:`, user: result.recordset[0] });
        } else {
            res.status(404).send(`Profile not found for :${req.user.username}:`);
        }
    } catch (err) {
        console.error(err);
        res.status(500).send(`Error fetching Profile for :${req.user.username}:`);
    }
});

function generateAccessToken(user) {
    return jwt.sign(user, process.env.ACCESS_TOKEN_SECRET, {expiresIn: '15m'});
}

module.exports = router;