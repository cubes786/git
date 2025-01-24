console.log('Server sript is starting....');

const express=require('express')
const cors=require('cors')
require('dotenv').config();
const booksRouter=require('./routes/books');
const usersRoute=require('./routes/users');
const ordersRoute=require('./routes/orders');
const { initializePool } = require('../shared/db');

const app=express();
const port=process.env.PORT || 3001;

//debug statments start
// console.log("DB_SERVER:", process.env.DB_SERVER)
// console.log("Type:",typeof process.env.DB_SERVER);
// console.log('USERNAME:', process.env.USERNAME);
// const os = require('os');
// const userInfo = os.userInfo();
// console.log('User Info:', userInfo);
// console.log('USER:', process.env.USER);
//debug statments end

app.use(cors());
app.use(express.json()); //enable JSON body parsing

// Initialize the connection pool
initializePool();

//Routes
app.use('/', booksRouter);
app.use('/', usersRoute);
app.use('/', ordersRoute);

app.get('/', (req, res)=>{
    res.send('Hello World')
})

app.listen(port, ()=> {
    console.log(`Server is running on port ${port}`);
});

console.log("Server script is ending...")