const https = require('https')

const start = Date.now()

// the https request is delegated to the OS, and it decides how many threads to use
const doRequest = () =>
    https.request('https://google.com', res => {
        res.on('data', () => {})
        res.on('end', () => {
            console.log(Date.now() - start)
        })
    }).end()

doRequest();
doRequest();
doRequest();
doRequest();
doRequest();
doRequest();
doRequest();
doRequest();