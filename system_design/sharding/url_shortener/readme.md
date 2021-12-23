docker build -t pgshard .
docker run --name pgshard1 -p 5432:5432 -d -e POSTGRES_PASSWORD=password pgshard
docker run --name pgshard2 -p 5433:5432 -d -e POSTGRES_PASSWORD=password pgshard
docker run --name pgshard3 -p 5434:5432 -d -e POSTGRES_PASSWORD=password pgshard
docker pull dpage/pgadmin4
docker run --name pgadmin -d -e PGADMIN_DEFAULT_EMAIL=alicedeadbride@gmail.com -e PGADMIN_DEFAULT_PASSWORD=user1_test -p 5555:80 dpage/pgadmin4


#### insert url into db
```js
await (await fetch('http://localhost:8081/?url=https://wikipedia.com/sharding', {method: 'POST'})).json()
```
#### push a lot of urls into db
```js
Array.from(Array(10).keys()).forEach(i => fetch(`http://localhost:8081/?url=https://google.com/?q=${i}`, {method: 'POST'}).then(x => x.json()).then(x => console.log(x)))
```
#### query url from db
```js
await (await fetch('http://localhost:8081/?fuJis')).json()
```