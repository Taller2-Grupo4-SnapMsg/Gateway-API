docker build -t gateway .
docker run -e USERS_URL=$USERS_URL -p 8080:8080 gateway