# How to run:

docker-compose up --build

# Tạo migrate cho api-express:

Tạo model và migration: npx sequelize-cli model:generate --name User --attributes name:string

Chạy migration: npx sequelize-cli db:migrate


# CRUD API api-express:

1/ Tạo user

curl --location 'http://127.0.0.1:3000/users/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Quang2"
}'

2/ Show list Users

curl --location 'http://127.0.0.1:3000/users/'


3/ Xem chi tiết User với id

curl --location 'http://127.0.0.1:3000/users/1'

4/ Cập nhật thông tin User với id

curl --location --request PUT 'http://127.0.0.1:3000/users/1' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Quang2"
}'

5/ Xóa User

curl --location --request DELETE 'http://127.0.0.1:3000/users/1'