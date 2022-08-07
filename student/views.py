from django.shortcuts import render
from .models import Student,Teacher
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################
def student_list_(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})


# Filter and OR query
def student_list_(request):

    # posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')
    posts = Student.objects.filter (Q(surname__startswith='austin') | Q (surname__startswith='baldwin'))
# 

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})



# and query
def student_list_(request):

    # posts = Student.objects.filter(classroom=3) & Student.objects.filter(surname__startswith='baldwin')
    posts = Student.objects.filter (Q(classroom=3) & Q (surname__startswith='baldwin'))
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

# union query
def student_list_(request):
    # posts=Student.objects.all().values_list('firstname').union(Teacher.objects.all().values_list('firstname'))
    posts=Student.objects.all().values('firstname').union(Teacher.objects.all().values('firstname'))
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

# NOT Query
# exclude 
def student_list_(request):
    # posts=Student.objects.exclude(age=20)
    posts=Student.objects.exclude(age__gt=20)

    # gt
    # gte
    # lt
    # lte
    
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})
# Filter
def student_list_(request):

    posts=Student.objects.filter(~Q(age=20) & ~Q(firstname='raquel'))
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})


# SELECT and OutPut Individual field
def student_list_(request):
    posts=Student.objects.filter(age=20).only('firstname','age')
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'data':posts})



# Simple performing raw query
def student_list(request):
    sql="SELECT * FROM student_student"
    posts=Student.objects.raw(sql)
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'data':posts})























# def student_list_(request):
#     posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html',{'posts':posts})

# def student_list(request):
#     posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q (surname__startswith='baldwin') | Q (surname__startswith='avery-parker'))

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html',{'posts':posts})