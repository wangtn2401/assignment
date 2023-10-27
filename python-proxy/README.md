Check python proxy:

## Get list users:

curl --location 'http://127.0.0.1:8000/users/?limit=2&offset=1' 

# Get user detail:

curl --location 'http://127.0.0.1:8000/users/<int:user_id>'