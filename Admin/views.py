from django.http import HttpResponse
from django.shortcuts import render
from .models import Department, AcademicYear, Login

# Create your views here.

def admin_view(request):
    return render(request, 'Admin/home.html')


def admin_changepd(request):
    return render(request, 'Admin/changepd.html')


def display_view(request):
    return render(request, 'Admin/Adminhome.html')


def display_desig(request):
    results = Department.objects.all()
    return render(request, 'Admin/desig.html', {'Department': results})


def dispaly_changeacdyear(request):
    results = AcademicYear.objects.all()
    return render(request, 'Admin/changeacdyear.html', {'AcademicYear': results})


def display_changeacd(request):
    return render(request, 'Admin/changeacd.html')


def admin_pplfacultydetails(request):
    return render(request, 'Admin/pplfacultydetails.html')


def login(request):

        return render(request, 'Admin/home.html')


def index(request):
    return render(request, 'Admin/Adminhome.html')
























