from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homepage_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
    my_context = {
        "my_text" : "this is about me",
        "my_number" : 1234,
        "my_list" : [123,456,789],
        "my_html" : "<h1>hello world</h1>"
    }
    print(args,kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"contact.html",my_context)
