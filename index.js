const express = require('express')
const cors = require('cors')
const port = 3000
const request = require('request')

const app = express()

app.use(cors())

app.listen(port, () => console.log('Spinning up incub8'))