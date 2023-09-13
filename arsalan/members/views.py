from django.shortcuts import render, redirect, get_object_or_404

from arsalan.members.serializer import ReactSerializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import React
from rest_framework import serializers


class ReactView(APIView):
    def get(self, request):
        detail=[{"name":detail.name,"email":detail.email}
        for detail in React.objects.all()]
        return Response(detail)
    
def post(self, request):
    serializer = ReactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Return a success response with status code 201 (Created)
    return Response(serializer.errors, status=400)  # Return a response with validation errors and status code 400 (Bad Request) if data is invalid


# def delete_user(request, user_id):
#     if request.method == 'POST':
#         user = get_object_or_404(User, pk=user_id)
#         user.delete()  # Delete the user record from the database
    
#     return redirect('user_form')  # Redirect to the original page
