from django.shortcuts import render # type: ignore

# Create your views here.
def home_view (request):
    return render(request, 'home.html')