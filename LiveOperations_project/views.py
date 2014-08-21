from django.http import HttpResponse

def index(request):
    return HttpResponse("Root index for Live Operations")
