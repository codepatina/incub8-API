const { Client } = require('pg')
require('dotenv').config()


const client = new Client({
    user: process.env.PGUSER,
    host: process.env.PGHOST,
    database: process.env.PGDATABASE,
    password: process.env.PGPASSWORD,
    port: process.env.PGPORT
})


client.connect()

client.query(`CREATE DATABASE ${process.env.PGDATABASE}`, (err, res) => {
    console.log(err, res)
    
    client.end()
})

// client.query(`DROP DATABASE ${process.env.PGDATABASE}`, (err, res) => {
//     console.log(err, res)
//     client.end()
// })