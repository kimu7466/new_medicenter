from django.shortcuts import render
from staff.views import staff_authenticated
from .models import doctor

def get_doctor_details(doctor_id=None):
    if not isinstance(doctor_id, type(doctor_id)):
        get_doctor = [doctor.objects.get(id=doctor_id)]
    else:
        get_doctor = doctor.objects.all().order_by('-id')
    return get_doctor

@staff_authenticated
def dashboard_view(request):
    context = {
        'total_doctors':get_doctor_details().count()
    }
    return render(request, 'dashboard.html', context)

@staff_authenticated
def doctors_view(request):
    context = {
        'doctors':get_doctor_details()
    }
    return render(request, 'doctors.html', context)

@staff_authenticated
def patients_view(request):
    context = {
        'doctors':get_doctor_details()
    }
    return render(request, 'patients.html',context)