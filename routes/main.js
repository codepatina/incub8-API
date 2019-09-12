const express = require('express')
const router = express.Router()

router.get('/', (req, res, err) => {
    res.send('Hello World!')
})

router.get('/ping', (req, res, err) => {
    res.send('Welcome to incub8')
})

module.exports = router

