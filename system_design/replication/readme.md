#### create a master & replica containers
```sh
docker run --name pgmaster -p 5432:5432 -v ~/Work/Dev/Git/ntbts/system_design/replication/master_data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=postgres -d postgres

docker run --name pgstandby -p 5433:5432 -v ~/Work/Dev/Git/ntbts/system_design/replication/standby_data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=postgres -d postgres

docker exec -it pgmaster psql -U postgres
docker exec -it pgstandby psql -U postgres
create table test (id int, t varchar(200));
```

note: replication set up didn't work for me for some reason, hence not leaving the config details here..