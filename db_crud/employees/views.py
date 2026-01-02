import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Employee


# READ - Get all employees
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        data = list(employees.values())
        return JsonResponse(data, safe=False)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


# CREATE - Create employee (POST JSON)
@csrf_exempt
def employee_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            employee = Employee.objects.create(
                name=data['name'],
                email=data['email'],
                age=data['age'],
                department=data['department']
            )

            return JsonResponse(
                {'message': 'Employee created', 'id': employee.id},
                status=201
            )

        except KeyError:
            return JsonResponse({'error': 'Missing fields'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


# UPDATE - Update employee by ID (PUT)
@csrf_exempt
def employee_update(request, id):
    if request.method in ['PUT', 'PATCH']:
        try:
            data = json.loads(request.body)
            emp = get_object_or_404(Employee, id=id)

            emp.name = data.get('name', emp.name)
            emp.email = data.get('email', emp.email)
            emp.age = data.get('age', emp.age)
            emp.department = data.get('department', emp.department)

            emp.save()

            return JsonResponse({'message': 'Employee updated'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


# DELETE - Delete employee
@csrf_exempt
def employee_delete(request, id):
    if request.method == 'DELETE':
        emp = get_object_or_404(Employee, id=id)
        emp.delete()
        return JsonResponse({'message': 'Employee deleted'})

    return JsonResponse({'error': 'Method not allowed'}, status=405)
