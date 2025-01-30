const express = require('express');
const router = express.Router();
const { getConnection } = require('../../shared/db');
const sql = require('mssql/msnodesqlv8');
const { authenticateToken } = require('../../shared/auth');

router.post('/orders', authenticateToken, getConnection, async (req, res) => {
    const { orderItems, totalAmount } = req.body; // Get totalAmount from the request body
    try {
      // req.user is populated by the authenticateToken middleware
      const userId = req.user.id;
        // Insert new order into Orders table with paymentStatus and totalAmount
        const orderResult = await req.pool.request()
            .input('userId', req.sql.Int, userId)
            .input('status', req.sql.VarChar, 'pending')  // Initial payment status
            .input('totalAmount', req.sql.Decimal(10, 2), totalAmount)  // Use the totalAmount from the frontend
            .query(
                'INSERT INTO BookSelling.Orders (userId, orderDate, orderStatus, paymentStatus, totalAmount) OUTPUT INSERTED.id VALUES (@userId, GETDATE(), @status, @status, @totalAmount)'
            );
        const orderId = orderResult.recordset[0].id;

        // Insert order items into OrderItems table
        for (let orderItem of orderItems) {
            await req.pool.request()
                .input('orderId', req.sql.Int, orderId)
                .input('bookId', req.sql.Int, orderItem.id)
                .input('quantity', req.sql.Int, orderItem.quantity)
                .query(
                    'INSERT INTO BookSelling.OrderItems (orderId, bookId, quantity) VALUES (@orderId, @bookId, @quantity)'
                );
        }

        res.status(201).json({ message: `Order Placed for order: ${orderId} and user: ${userId}`, orderId });
    } catch (err) {
        console.error(err);
        res.status(500).send('Error creating order');
    }
});

router.get('/orders', authenticateToken, getConnection, async (req, res) => {
    try {
        const result = await req.pool.request().query('SELECT * FROM BookSelling.Orders');
        res.json(result.recordset);
    } catch (err) {
        console.error(err);
        res.status(500).send('Error fetching orders');
    }
});

router.patch('/orders/:orderId/complete', authenticateToken, getConnection, async (req, res) => {
    console.log('Received request to complete order');
    console.log(`Request URL: ${req.url}`);
    console.log(`Request method: ${req.method}`);

    const { orderId } = req.params;
    const { transactionId, amount } = req.body;

    try {
        console.log(`Received request to mark order ${orderId} as paid`);

        // Fetch the order
        const orderResult = await req.pool.request()
            .input('orderId', req.sql.Int, orderId)
            .query('SELECT * from BookSelling.Orders WHERE id = @orderId');

        console.log(`Order result: ${JSON.stringify(orderResult.recordset)}`);

        if (orderResult.recordset.length === 0) {
            console.error(`Order not found: ${orderId}`);
            return res.status(404).send('Order not found');
        }

        // Use the same request pool to update the orders and payments tables
        await req.pool.request()
            .input('orderId', req.sql.Int, orderId)
            .input('status', req.sql.VarChar, 'paid')
            .query(`UPDATE BookSelling.Orders SET paymentStatus = @status WHERE id = @orderId`);

        console.log(`Updated order ${orderId} payment status to 'paid'`);

        await req.pool.request()
            .input('orderId', req.sql.Int, orderId)
            .input('transactionId', req.sql.NVarChar, transactionId)
            .input('amount', req.sql.Decimal(10, 2), amount)
            .input('status', req.sql.VarChar, 'successful')
            .query(`INSERT INTO BookSelling.Payments 
                    (orderId, transactionId, paymentMethod, paymentDate, amount, paymentStatus)
                    VALUES (@orderId, @transactionId, 'manual', GETDATE(), @amount, @status)`);

        console.log(`Inserted payment record for order ${orderId}`);

        res.json({ message: `Order ${orderId} marked as paid` });
    } catch (err) {
        console.error(`Error marking order ${orderId} as paid: ${err.message}`);
        console.error(`Error stack: ${err.stack}`);
        res.status(500).send('Error marking order as paid');
    }
});

module.exports = router;