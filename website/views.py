from django.http import HttpResponse


def index(_request):
    return HttpResponse("Hello, my lovely visitor. Welcome to this website.")


def detail(_request, blog_id):
    return HttpResponse("Hello, my lovely visitor. This is blog %s.", blog_id)

