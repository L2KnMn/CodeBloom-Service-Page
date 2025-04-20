#from django.http import HttpResponse
from django.shortcuts import render
from .models import MainContent

# Create your views here.
def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'product/content_list.html', context)


def detail(request, content_id):
    content_list = MainContent.objects.get(id=content_id)
    context = {'content_list': content_list}
    return render(request, 'product/detail.html', context)