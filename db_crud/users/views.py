import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import User


# READ - Get all employees
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        data = list(users.values())
        return JsonResponse(data, safe=False)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


# CREATE - Create employee (POST JSON)
@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            user = User.objects.create(
                name=data['name'],
                email=data['email'],
                age=data['age'],
                department=data['department']
            )

            return JsonResponse(
                {'message': 'User created', 'id': user.id},
                status=201
            )

        except KeyError:
            return JsonResponse({'error': 'Missing fields'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


# UPDATE - Update employee by ID (PUT)
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


# DELETE - Delete employee
@csrf_exempt
def user_delete(request, id):
    if request.method == 'DELETE':
        usr = get_object_or_404(User, id=id)
        usr.delete()
        return JsonResponse({'message': 'User deleted'})

    return JsonResponse({'error': 'Method not allowed'}, status=405)
