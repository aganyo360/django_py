from django.shortcuts import render
from . models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.is_true = False
    feature1.name = 'Slow'
    feature1.details = 'service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'efficient'
    feature2.is_true = False
    feature2.details = 'service is very efficient'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'reliable'
    feature3.is_true = True
    feature3.details = 'service is very reliable'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'steadfast'
    feature4.is_true = True
    feature4.details = 'service is very steadfast'

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'trustworthy'
    feature5.is_true = True
    feature5.details = 'service is very trustworthy'

    features = [feature1, feature2, feature3, feature4, feature5  ]

    return render(request, 'index.html', {'features':features})
