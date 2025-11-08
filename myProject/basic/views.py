from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import StudentNew
# Create your views here.

def sample(request):
    return HttpResponse('hello world')

def sample1(request):
    return HttpResponse('welcome to django')

def sampleInfo(request):
    # data={"name":'sumanth','age':25,'city':'hyd'}
    data={'result':[4,6,8,9]}
    return JsonResponse(data)

def dynamicResponse(request):
    name=request.GET.get("name",'kiran')
    city=request.GET.get("city",'hyd')
    
    return HttpResponse(f"hello {name} from {city}")

#to test database connection
def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})

@csrf_exempt
def addStudent(request):
    print(request.method)
    if request.method == "POST":
        data=json.loads(request.body)
        student=StudentNew.objects.create(
            name=data.get('name'),
            age=data.get("age"),
            email=data.get("email")
            )
        return JsonResponse({"status":"success","id":student.id},status=200)
    return JsonResponse({"error":"use post method"},status=400)



