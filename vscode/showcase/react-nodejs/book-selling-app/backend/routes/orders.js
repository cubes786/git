const express = require('express');
const router = express.Router();
const { getConnection } = require('../../shared/db');
const sql = require('mssql/msnodesqlv8');


router.post('/orders', getConnection, async (req, res) => {
    const { userId, orderItems } = req.body;
    try {
        const orderResult = await req.pool.request()
            .input('userId', req.sql.Int, userId)
            .input('status', req.sql.VarChar, 'pending')
            .query(
                'INSERT INTO BookSelling.Orders (userId, orderDate, orderStatus) OUTPUT INSERTED.id VALUES (@userId, GETDATE(), @status)'
            );
        const orderId = orderResult.recordset[0].id;

        // insert into OrderItems
        for (let orderItem of orderItems) {
            await req.pool.request()
                .input('orderId', req.sql.Int, orderId)
                .input('bookId', req.sql.Int, orderItem.id)
                .input('quantity', req.sql.Int, 1)
                .query(
                    'INSERT INTO BookSelling.OrderItems (orderId, bookId, quantity) VALUES (@orderId, @bookId, @quantity)'
                );
        }

        res.status(201).json({ message: `Order Placed for order:${orderId}: and user:${userId}`, orderId });
    } catch (err) {
        console.error(err);
        res.status(500).send(`Error creating order`);
    }
});

router.get('/orders', getConnection, async (req, res) => {
    try {
        const result = await req.pool.request().query('SELECT * FROM BookSelling.Orders');
        res.json(result.recordset);
    } catch (err) {
        console.error(err);
        res.status(500).send('Error fetching orders');
    }
});

module.exports = router;