from django.shortcuts import render # type: ignore

# Create your views here.
def home_view (request):
    return render(request, 'home.html')

def about_view (request):
    return render(request, 'about.html')

def project_view (request):
    return render(request, 'project.html')

