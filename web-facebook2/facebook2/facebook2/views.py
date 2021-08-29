from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

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
        'posts': postlist
    }

    # return HttpResponse(profilepage)
    return render(request, 'facebook2/profile.html', context)

def article(request, id=1):
    articlepage = '<h1> Showing you article ' + str(id) + ' </h1>'
    return HttpResponse(articlepage)