const app = require('express')();
const { Client } = require('pg');
const crypto = require('crypto');
const HashRing = require('hashring');

const hr = new HashRing();
hr.add('5432');
hr.add('5433');
hr.add('5434');

const clients = {
    5432: new Client({
        host: 'lisss-MacBook-Pro.local',
        port: '5432',
        user: 'postgres',
        password: 'password',
        database: 'postgres',
    }),
    5433: new Client({
        host: 'lisss-MacBook-Pro.local',
        port: '5433',
        user: 'postgres',
        password: 'password',
        database: 'postgres',
    }),
    5434: new Client({
        host: 'lisss-MacBook-Pro.local',
        port: '5434',
        user: 'postgres',
        password: 'password',
        database: 'postgres',
    }),
};
connect();
async function connect() {
    await clients['5432'].connect();
    await clients['5433'].connect();
    await clients['5434'].connect();
}

app.get('/:urlId', async (req, res) => {
    const urlId = req.params.urlId;

    const server = hr.get(urlId);
    const result = await clients[server].query(
        'select * from url_table where url_id = $1',
        [urlId]
    );
    if (result.rowCount) {
        res.send({
            result: result.rows[0],
            server,
        });
    } else {
        res.sendStatus(404);
    }
});
app.post('/', async (req, res) => {
    const url = req.query.url;

    // consistent hashing
    const hash = crypto.createHash('sha256').update(url).digest('base64');
    const urlId = hash.substr(0, 5);

    const server = hr.get(urlId);
    await clients[server].query(
        'insert into url_table (url, url_id) values ($1, $2)',
        [url, urlId]
    );
    res.send({
        hash,
        urlId,
        server,
    });
});

app.listen(8081, () => console.log('Listening on 8081...'));
