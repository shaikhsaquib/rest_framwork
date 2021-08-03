from django.http.response import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

# from rest_fram.api import serializers

# Create your views here.
def student_detials(request, pk):
    stu=Student.objects.get(id=pk)
    print(stu)
    serializer=StudentSerializer(stu)
    print(serializer)
    json_data=JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')

# query set all student data
def student_list(request):
    stu=Student.objects.all()
    print(stu)
    serializer=StudentSerializer(stu,many=True)
    print(serializer)
    json_data=JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')