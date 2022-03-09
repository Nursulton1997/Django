from django.shortcuts import render

# Create your views here.

def index(requests):
    return render(requests, 'dashboard/examples/start-template.html', {})