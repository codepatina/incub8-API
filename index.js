const express = require('express')
const cors = require('cors')
const port = 3000
const request = require('request')
const router = require('./routes/main.js')
require('dotenv').config()

const Sequelize = require('sequelize');

const sequelize = new Sequelize(
    process.env.DATABASE,
    process.env.USER,
    process.env.PASSWORD,
    {
        dialect: 'postgres'
    }
)
const app = express()

app.use(cors())

app.use('/', router)


app.listen(port, () => console.log('Spinning up incub8'))

sequelize
    .authenticate()
    .then(() => {
        console.log('Connection has been established successfully.');
    })
    .catch(err => {
        console.error('Unable to connect to the database:', err);
    });


