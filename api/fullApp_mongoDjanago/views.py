from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Department, Employee
from .serializers import DepartmentSerializers, EmployeeSerializers
from django.core.files.storage import default_storage


@csrf_exempt
def departmentAPI(request, id=0):
    if request.method=='GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializers(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializers(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(depId=department_data['depId'])
        departments_serializer = DepartmentSerializers(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully!!" , safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    
    elif request.method == 'DELETE':
        department = Department.objects.get(depId=id)
        department.delete()
        return JsonResponse("Deleted Successfully!!" , safe=False)    
    

@csrf_exempt
def employeeAPI(request, id=0):
    if request.method=='GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializers(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializers(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(empId=employee_data['empId'])
        employees_serializer = EmployeeSerializers(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully!!" , safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    
    elif request.method == 'DELETE':
        employee = Employee.objects.get(empId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully!!" , safe=False)    
    
    
@csrf_exempt
def saveFile(request):
    files = request.FILES['file']
    files_name = default_storage.save(files.name, files)
    return JsonResponse(files_name, safe=False)


