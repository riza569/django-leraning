from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status,mixins,generics 

class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

# class Employees(APIView):
    
#     def get(self,request):
#         employee=Employee.objects.all()
#         serializer=EmployeeSerializer(employee,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
     
#         serializer=EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
        
        
class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
        queryset=Employee.objects.all()
        serializer_class=EmployeeSerializer
        
        def get(self,request,pk):
            return self.retrieve(request,pk)
        
        def put(self,request,pk):
            return self.update(request,pk)
        
        def delete(self,request,pk):
            return self.destroy(request,pk)
        
        
        
        
        
# class EmployeeDetail(APIView):
    
    
#     def get(self,request,pk):
#         employee=get_object_or_404(Employee,pk=pk)      
#         serializer=EmployeeSerializer(employee)
#         return Response(serializer.data)
    
    
#     def put(self,request,pk):
#         employee=get_object_or_404(Employee,pk=pk)     
#         serializer=EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors) 
    
#     def delete(self,request,pk):
#         employee=get_object_or_404(Employee,pk=pk)     
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        