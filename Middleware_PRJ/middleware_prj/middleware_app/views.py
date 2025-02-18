from django.shortcuts import render
from .models import Employee
from django.db.models import Sum
from django.db.models import Q


def get(request):
    queryset=Employee.objects.filter(Q(salary__gt=50000) & Q(salary__lt=100000))    
    #object.filter.q
    print(queryset)
    return render(request, 'index.html', {'queryset':queryset}) 
