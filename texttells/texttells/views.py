from django.http import HttpResponse

def index(request):
    return HttpResponse("hello Hridoy")


def about(request):
    return HttpResponse("This is aboout")