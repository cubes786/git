console.log('Server sript is starting....');

const express=require('express')
const cors=require('cors')
require('dotenv').config();
const booksRouter=require('./routes/books');
const usersRoute=require('./routes/users');
const ordersRoute=require('./routes/orders');
const paymentsRoute=require('./routes/payments');
const { initializePool } = require('../shared/db');

const app=express();
const port=process.env.PORT || 3001;

app.use(cors());
app.use(express.json()); //enable JSON body parsing

// Initialize the connection pool
initializePool();

//Routes
app.use('/', booksRouter);
app.use('/', usersRoute);
app.use('/', ordersRoute);
app.use('/', paymentsRoute);

app.get('/', (req, res)=>{
    res.send('Hello World')
})

app.listen(port, ()=> {
    console.log(`Server is running on port ${port}`);
});

console.log("Server script is ending...")