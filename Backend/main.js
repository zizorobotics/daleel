const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    res.send('I am here on localhost:3000!');
});

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});
