from django.shortcuts import render

# Create your views here.
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from rest_framework.views import APIView
from django.contrib.auth.models import Response

class TaskListCreateView(generics.ListCreateAPIView):
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=['category']
    search_fields=['title']
    ordering_fields=['amount']
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=['category']
    search_fields=['title']
    ordering_fields=['amount']
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class ExpenseView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        total=Expense.object.filter(user=request.user).aggregate(total_Expense=sum('amount'))
        return Response(total)
