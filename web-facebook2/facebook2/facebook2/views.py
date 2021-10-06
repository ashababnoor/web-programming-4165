from django.core.checks import messages
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from .models import Appointment, Post

def home(request):
    homepage = '''

    <h1>Welcome person! </h1>
    <p> This is a paragraph</p>

    '''
    # return HttpResponse(homepage + '<p>' + str(dir(request.get_host())) + '</p>')

    context = {
        'username': 'Shabab'
    }

    return render(request, 'facebook2/index.html', context)

def about(request):
    return render(request, 'facebook2/about.html')

def profile(request):
    profilepage = '''
    
    <p> My student Id is 011 193 024 <br>
    My name is Ahmed Shabab Noor </p>

    '''

    postlist = [
        {
            'content': 'Hello this is the first post',
            'author': 'Shabab Noor',
            'date': '30/08/21',
            'tags': ['fun', 'exciting']
        },
        {
            'content': 'Oh hi! This is the second post',
            'author': 'Mr. Noor',
            'date': '31/08/21',
            'tags': ['fun', 'exciting', 'old']
        },
        {
            'content': 'This is just another post',
            'author': 'Random User',
            'date': '31/08/21',
            'tags': ['meh', 'boring', 'old']
        }
    ]

    context = {
        'posts': Post.objects.all()
    }

    # return HttpResponse(profilepage)
    return render(request, 'facebook2/profile.html', context)

def article(request, id=1):
    articlepage = '<h1> Showing you article ' + str(id) + ' </h1>'
    return HttpResponse(articlepage)


def bookappt(request):
    if (request.method == 'GET'):
	    return render(request, 'apptservice/bookappt.html')
    elif (request.method == 'POST'):
        doctor = request.POST.get('doctor_name', '')
        patient = request.POST.get('patient_name', '')
        date = request.POST.get('pref_date', '')
        phone = request.POST.get('phone_no', '')

        appt = Appointment(preferred_date=date, doctor_name=doctor, patient_name=patient, phone_no=phone)
        appt.save()

        # getting the last appointment by specified doctor
        last_appt = Appointment.objects.filter(doctor_name=doctor).order_by('-preferred_date').first()
        # getting total appointments of specified doctor on the same date as the last appt
        serial = Appointment.objects.filter(doctor_name=doctor).filter(preferred_date = last_appt.preferred_date).count() + 1

        message = "Your serial number is " + serial
        return HttpResponse(message)


    if (request.method == 'GET'):
        return render(request, 'facebook2/signin.html')
    elif (request.method == 'POST'):
        u = request.POST.get('user', '')
        p = request.POST.get('pass', '')
        user = authenticate(username=u, password=p)
        if user is None:
            messages.error(request, 'Invalid username or password')
            # messages.info(request, 'extra info')
            return render(request, 'facebook2/signin.html')
        else:
            login(request, user)
            return redirect('home-page')