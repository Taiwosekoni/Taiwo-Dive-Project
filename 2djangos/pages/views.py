from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Hello, world. You're at the pages index.") 