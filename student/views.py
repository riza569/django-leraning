from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.


@api_view(['GET',"POST"])
def StudentView(request):
    
    if request.method=="GET":
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
    
    elif request.method=="POST":
        
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(["GET","PUT","DELETE"])
def StudentDetail(request,pk):
    student=get_object_or_404(Student,pk=pk)
    
    if request.method=="GET":
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    elif request.method=="PUT":
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)