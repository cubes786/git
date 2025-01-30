const express = require('express');
const router = express.Router();
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const { authenticateToken } = require('../../shared/auth');
const { getConnection } = require('../../shared/db');
const sql = require('mssql/msnodesqlv8');

// Create Payment Intent
router.post('/payment-intents', authenticateToken, getConnection, async (req, res) => {
    console.log("🟢 /payment-intents route hit!");  // ✅ This should always appear
    console.log("Request body:", req.body);  // Log incoming request
    console.log("User from token:", req.user);  // Log authenticated user

    try {
        const { orderId } = req.body;
        const userId = req.user.id; //userId

        console.log(`Received request for payment intent: orderId=${orderId}, userId=${userId}`);

        // Get order details
        const query = `SELECT id, totalAmount FROM BookSelling.Orders 
                       WHERE id = @orderId AND userId = @userId AND paymentStatus = 'pending'`;

        console.log(`Executing SQL Query:\n${query}`);
        console.log(`Parameters: orderId=${orderId}, userId=${userId}`);

        const orderResult = await req.pool.request()
            .input('orderId', sql.Int, orderId)
            .input('userId', sql.Int, userId)
            .query(query);

        console.log("SQL Query Result:", orderResult.recordset);

        if (orderResult.recordset.length === 0) {
            console.error(`❌ Order not found: orderId=${orderId}, userId=${userId}`);
            return res.status(404).json({ error: `Order not found: orderId=${orderId}, userId=${userId}` });
        }

        const order = orderResult.recordset[0];
        const amount = Math.round(order.totalAmount * 100); // Convert to cents

        console.log(`💰 Creating Stripe Payment Intent for amount: ${amount} cents`);

        // Create Payment Intent
        const paymentIntent = await stripe.paymentIntents.create({
            amount: amount,
            currency: 'usd',
            metadata: { orderId: orderId.toString() }
        });

        console.log("✅ Stripe Payment Intent Created:", paymentIntent);

        res.json({ clientSecret: paymentIntent.client_secret });
    } catch (err) {
        console.error("🔥 ERROR creating payment intent:", err);
        res.status(500).send('Error creating payment intent');
    }
});

// Stripe Webhook Handler
router.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
    const sig = req.headers['stripe-signature'];
    let event;

    try {
        event = stripe.webhooks.constructEvent(
            req.rawBody,
            sig,
            process.env.STRIPE_WEBHOOK_SECRET
        );
    } catch (err) {
        console.error('Webhook error:', err.message);
        return res.status(400).send(`Webhook Error: ${err.message}`);
    }

    // Handle payment success
    if (event.type === 'payment_intent.succeeded') {
        const paymentIntent = event.data.object;
        const orderId = parseInt(paymentIntent.metadata.orderId);

        try {
            const pool = await sql.connect();
            await pool.request()
                .input('orderId', sql.Int, orderId)
                .input('status', sql.VarChar, 'paid')
                .query(`UPDATE BookSelling.Orders SET paymentStatus = @status WHERE id = @orderId`);

            await pool.request()
                .input('orderId', sql.Int, orderId)
                .input('transactionId', sql.NVarChar, paymentIntent.id)
                .input('amount', sql.Decimal(10, 2), paymentIntent.amount / 100)
                .input('status', sql.VarChar, 'successful')
                .query(`INSERT INTO BookSelling.Payments 
                       (orderId, transactionId, paymentMethod, paymentDate, amount, paymentStatus)
                       VALUES (@orderId, @transactionId, 'stripe', GETDATE(), @amount, @status)`);
        } catch (err) {
            console.error('Database update error:', err);
        }
    }

    res.json({ received: true });
});

module.exports = router;