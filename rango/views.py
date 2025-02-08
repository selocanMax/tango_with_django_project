from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")  # ✅ Test bunu bekliyor!

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")  # ✅ Test bunu bekliyor!
