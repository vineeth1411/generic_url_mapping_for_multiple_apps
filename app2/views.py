from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
def app2_string(request):
    return HttpResponse('<h1><b>app2_string as responce</b></h1>')


def app2_htmlpage(request):
    return render(request,'app2_htmlpage.html')