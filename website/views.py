from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def detail(_request, blog_id):
    return HttpResponse(f'Hello, my lovely visitor. This is blog {blog_id}.')

