// frontend/src/components/CheckoutForm.js
import React, { useState, useEffect } from 'react';
import { useCart } from '../contexts/CartContext';
import { useNavigate } from 'react-router-dom';
import { Card, Form, Button, Container, Spinner, Alert } from 'react-bootstrap';
import { loadStripe } from '@stripe/stripe-js';
import { Elements, CardElement, useStripe, useElements } from '@stripe/react-stripe-js';
import axios from 'axios';

const STRIPE_PUBLISHED_KEY = 'pk_test_51QlkpwCFYjIgmAA6hkDRShKbboHsMJZmFrZlWEG74vVk38WhnbzxsmWsPnnR1RbZ3dPGqUCAdY0bIqltxrtZYyUm00VA4lBrEB';
const stripePromise = loadStripe(STRIPE_PUBLISHED_KEY);

const CheckoutForm = () => {
    const { cart, clearCart } = useCart();
    const navigate = useNavigate();
    const stripe = useStripe();
    const elements = useElements();
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [clientSecret, setClientSecret] = useState(null);

    const calculateTotal = () => cart.reduce((total, item) => total + item.price * item.quantity, 0);
    const [orderId, setOrderId] = useState(null);

    useEffect(() => {
        const fetchPaymentIntent = async () => {
            const user = JSON.parse(sessionStorage.getItem('user'));
            const token = sessionStorage.getItem('token');

            if (!user || !token) return;

            try {
                const orderResponse = await axios.post('http://localhost:3001/orders', {
                    orderItems: cart,
                    totalAmount: calculateTotal()
                }, {
                    headers: { Authorization: 'Bearer ' + token }
                });
                
                const paymentResponse = await axios.post('http://localhost:3001/payment-intents', {
                    orderId: orderResponse.data.orderId
                }, {
                    headers: { Authorization: 'Bearer ' + token }
                });
                
                setOrderId(orderResponse.data.orderId); // Store the orderId
                setClientSecret(paymentResponse.data.clientSecret);
            } catch (err) {
                setError('Failed to load payment details. Please try again.');
            }
        };
        fetchPaymentIntent();
    }, []);

    const handleSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setError(null);

        if (!stripe || !elements) return;

        const cardElement = elements.getElement(CardElement);
        const { paymentIntent, error } = await stripe.confirmCardPayment(clientSecret, {
            payment_method: { card: cardElement }
        });

        if (error) {
            setError(error.message);
            setLoading(false);
            return;
        }
        
        if (paymentIntent.status === 'succeeded') {
            // Payment successful, call the /orders/:orderId/complete API
            try {
                const token = sessionStorage.getItem('token');
                const response = await axios.patch(`http://localhost:3001/orders/${orderId}/complete`, {
                    transactionId: paymentIntent.id,
                    amount: paymentIntent.amount / 100 // Convert amount from cents to dollars
                }, {
                    headers: { Authorization: 'Bearer ' + token }
                });
                console.log('Order completed successfully:', response.data);
            } catch (err) {
              console.error('Error completing order:', err);
            }
          } else {
            setError('Payment failed. Please try again.');
        }

        clearCart();
        navigate('/success');
    };

    if (cart.length === 0) return <Alert variant="warning">You need to add books before checking out.</Alert>;

    return (
        <Container className="d-flex justify-content-center align-items-center" style={{ minHeight: '70vh' }}>
            <Card style={{ width: '400px', padding: '20px' }}>
                <Card.Body>
                    <h2 className="text-center mb-4">Checkout</h2>
                    {error && <Alert variant="danger">{error}</Alert>}
                    {!clientSecret ? (
                        <Spinner animation="border" />
                    ) : (
                        <Form onSubmit={handleSubmit}>
                            <Form.Group className="mb-3">
                                <Form.Label>Card Details</Form.Label>
                                <CardElement className="form-control p-2" options={{ hidePostalCode: true }} />
                            </Form.Group>
                            <Button variant="primary" type="submit" className="w-100" disabled={loading}>
                                {loading ? 'Processing...' : 'Pay Now'}
                            </Button>
                        </Form>
                    )}
                </Card.Body>
            </Card>
        </Container>
    );
};

const Checkout = () => (
    <Elements stripe={stripePromise}>
        <CheckoutForm />
    </Elements>
);

export default Checkout;
