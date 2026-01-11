import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from .middleware import jwt_authenticate

# READ - Get all user
def user_list(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        auth_user = jwt_authenticate(request)
        users = User.objects.all()
        data = list(users.values())
        return JsonResponse(data, safe=False)

    except AuthenticationFailed as e:
        return JsonResponse({'error': str(e)}, status=401)


# CREATE - Create user (POST JSON)
@csrf_exempt
def user_register(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            hash_pssword = make_password(password)
            email = data.get('email')

            if not username or not password:
                return JsonResponse({'error': 'username and password required'}, status=400)
            if User.objects.filter(name=username).exists():
                return JsonResponse({'error': 'User already exists'}, status=400)
        
            user = User.objects.create(
                name=username,
                email=email,
                password=hash_pssword,
                department=data['department']
            )

            return JsonResponse(
                {'message': 'User created', 'id': user.id},
                status=201
            )

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

# Login - Login user with jwt
@csrf_exempt
def user_login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return JsonResponse(
                { 'error': 'Email and password are required' },
                 status= 400
            )
        
        try:
            user = User.objects.get(email= email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=401)
        
        if not check_password(password, user.password):
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
        
        # serializer = UserSerializer(user)
        refresh = RefreshToken()
        refresh['user_id'] = user.id
        refresh['email'] = user.email

        return JsonResponse({
            'data': {
                'user_id': user.id,
                'username': user.name,
                'email': user.email,
                'department': user.department
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        })

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=405)

# UPDATE - Update user by ID (PUT)
@csrf_exempt
def user_update(request, id):
    if request.method in ['PUT', 'PATCH']:
        try:
            data = json.loads(request.body)
            usr = get_object_or_404(User, id=id)

            usr.name = data.get('name', usr.name)
            usr.email = data.get('email', usr.email)
            usr.age = data.get('age', usr.age)
            usr.department = data.get('department', usr.department)

            usr.save()

            return JsonResponse({'message': 'User updated'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


# DELETE - Delete user
@csrf_exempt
def user_delete(request, id):
    if request.method == 'DELETE':
        usr = get_object_or_404(User, id=id)
        usr.delete()
        return JsonResponse({'message': 'User deleted'})

    return JsonResponse({'error': 'Method not allowed'}, status=405)
