from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .models import Account, Student, Professor, Prepmaterials
from .serializers import StudentSerializer, AccountSerializer, ProfessorSerializer, MaterialSerializer

from rest_framework import request
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class MaterialsViewSet(viewsets.ModelViewSet):
    queryset = Prepmaterials.objects.all()
    serializer_class = MaterialSerializer
