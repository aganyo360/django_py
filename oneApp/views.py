from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def innerpage(request):
    return render(request ,'inner-page.html')
def portfoliodetails(request):
    return render(request, 'portfoliodetails.html')