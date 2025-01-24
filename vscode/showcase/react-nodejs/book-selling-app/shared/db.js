// shared/db.js
const sql = require('mssql/msnodesqlv8');
require('dotenv').config();

// SQL Server connection config - use environment variables
const config = {
    connectionString: `DSN=${process.env.DSN_NAME};Database=${process.env.DB_NAME};Trusted_Connection=yes;` // Use the DSN you created
};
let pool;
let poolInitialized = false; // added global variable to ensure initialization happens only once

// Initialize the connection pool
async function initializePool() {
  if(!poolInitialized){
    try {
        pool = await sql.connect(config);
        console.log('SQL Server connection pool initialized');
         poolInitialized = true;
    } catch (err) {
        console.error('Error initializing SQL Server connection pool:', err);
        throw err; // Re-throw to stop the app if cannot connect to database
      }
   }
}

// Middleware to get connection from the pool for each API request
async function getConnection(req, res, next) {
    let connection;
    try {
        connection = await pool.connect();
        req.sql = sql;
        req.pool = pool;
        next();
    }
    catch (err) {
        console.error('Error getting sql connection', err);
        res.status(500).send('Error getting sql connection');
    }
    finally {
        if (connection) {
            try {
                await connection.release();
            }
            catch (releaseError) {
                console.error('Error releasing connection', releaseError);
            }
        }
    }
}

module.exports = {
    initializePool,
    getConnection
};