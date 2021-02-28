const https = require('https')
const crypto = require('crypto');
const fs = require('fs');

const start = Date.now()

// the https request is delegated to the OS, and it decides how many threads to use
const doRequest = () =>
    https.request('https://google.com', res => {
        res.on('data', () => {})
        res.on('end', () => {
            console.log(Date.now() - start)
        })
    }).end()


const doHash = () => crypto.pbkdf2('a', 'b', 100000, 512, 'sha512', () => {
    console.log('>> Hash:', Date.now() - start)
})

doRequest();

// here, fs makes 2 ticks:
// 1) go to HD and check file stats
// 2) read the file
// hence it waits in the thread pool after the 1st call to HD
// until the 1st hash calculation is done and a thread gets free
fs.readFile('multitask.js', 'utf8', () => {
    console.log('FS:', Date.now() - start)
})

doHash();
doHash();
doHash();
doHash();