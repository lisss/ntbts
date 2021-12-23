docker build -t pgshard .
docker run --name pgshard1 -p 5432:5432 -d -e POSTGRES_PASSWORD=password pgshard
docker run --name pgshard2 -p 5433:5432 -d -e POSTGRES_PASSWORD=password pgshard
docker run --name pgshard3 -p 5434:5432 -d -e POSTGRES_PASSWORD=password pgshard
docker pull dpage/pgadmin4
docker run --name pgadmin -d -e PGADMIN_DEFAULT_EMAIL=alicedeadbride@gmail.com -e PGADMIN_DEFAULT_PASSWORD=user1_test -p 5555:80 dpage/pgadmin4