
# Create migration for api-express:

Create models and migrations: npx sequelize-cli model:generate --name User --attributes name:string

Run migrations: npx sequelize-cli db:migrate


1/ Create user

curl --location 'http://127.0.0.1:3000/users/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Quang2"
}'

2/ Show list Users

curl --location 'http://127.0.0.1:3000/users/'


3/ Detail User with id

curl --location 'http://127.0.0.1:3000/users/<int:id>'

4/ Update User with id

curl --location --request PUT 'http://127.0.0.1:3000/users/<int:id>' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Quang2"
}'

5/ Delete User

curl --location --request DELETE 'http://127.0.0.1:3000/users/<int:id>'