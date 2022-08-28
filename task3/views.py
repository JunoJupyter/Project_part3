from django.shortcuts import render
from django.http import HttpResponse

cards= [
    {
        "imglink": 'static/task3/images/mt. fuji.jpg',
        "likes": 28,
    },
    {
        "imglink": 'static/task3/images/mt. fuji.jpg',
        "likes": 54,
    },
    {
        "imglink": 'static/task3/images/mt. fuji.jpg',
        "likes": 63,
    },
    {
        "imglink": 'static/task3/images/mt. fuji.jpg',
        "likes": 22,
    },
    {
        "imglink": 'static/task3/images/mt. fuji.jpg',
        "likes": 9,
    },
    
]

def index(request):
    return render(request,'task3/index.html')

def home(request):
    return render(request,'task3/homepage.html')

def myposts(request):
    return render(request,'task3/myposts.html',context={"cards": cards})

def newpost(request):
    return render(request,'task3/newpost.html')

# Create your views here.
