from django.http import JsonResponse
import requests

def get_users_from_proxy(request):
    proxy_url = "http://python-proxy:5000/users" 
    response = requests.get(proxy_url)
    users = response.json()
    return JsonResponse(users, safe=False)

def get_detail_user_from_proxy(request, user_id):
    proxy_url = "http://python-proxy:5000/users/" + str(user_id) 
    response = requests.get(proxy_url)
    users = response.json()
    return JsonResponse(users, safe=False)