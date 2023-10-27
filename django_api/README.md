# 1/ Create product

curl --location 'http://127.0.0.1:8000/products/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Old Phone",
    "price": 1001.50,
    "description": "in stock"
}'

# 2/ Show list Product

curl --location --request GET 'http://127.0.0.1:8000/products/?page=1&page_size=10'

# 3/ Detail Product with id

curl --location --request GET 'http://127.0.0.1:8000/products/<int:product_id>/'

# 4/ Update Product with id

curl --location --request PUT 'http://127.0.0.1:8000/products/<int:product_id>/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Old Phone",
    "price": 1001.50,
    "description": "in stock"
}'

# 5/ Delete Product

curl --location --request DELETE 'http://127.0.0.1:8000/products/<int:product_id>/'