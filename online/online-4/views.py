from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def result(request):
    context = {
        'names': ['Ervin', 'Bret', 'Graham', 'Victor', 'Jacobson']
    }

    return render(request, 'demoproject/result.html', context)

def details(request, name):
    studentList = {
        'Ervin': {
            'name': 'Ervin',
            'attendance': '87%',
            'mid': '16.5',
            'final': '22'
        },
        'Bret': {
            'name': 'Bret',
            'attendance': '92%',
            'mid': '15',
            'final': '23.5'
        },
        'Graham':{
            'name': 'Graham',
            'attendance': '84%',
            'mid': '18.5',
            'final': '21'
        },
        'Victor':{
            'name': 'Victor',
            'attendance': '95%',
            'mid': '19',
            'final': '24'
        },
        'Jacobson':{
            'name': 'Jacobson',
            'attendance': '91%',
            'mid': '17',
            'final': '22.5'
        }
    }

    context = {}
    if name in studentList.keys():
        context = studentList[name]
    
    return render(request, 'demoproject/details.html', context)
    