process.env.UV_THREADPOOL_SIZE = 1;
const cluster = require('cluster');

if (cluster.isMaster) {
    // cause index.js to be executed *again* but in child mode
    cluster.fork();
    cluster.fork();
    cluster.fork();
    cluster.fork();
    // it works best if the number of child processes is equal to num of CPU cores
} else {
    // i'm a child
    const express = require('express');
    const crypto = require('crypto');

    const app = express();

    app.get('/', (req, res) => {
        crypto.pbkdf2('a', 'b', 100000, 512, 'sha512', () => {
            res.send('Hi there!');
        })
    })

    app.get('/fast', (req, res) => {
        res.send('This was fast!')
    })

    app.listen(3000);
}