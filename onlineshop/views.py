from django.shortcuts import render

from onlineshop.models import CarBrand, CarModel, CarModelInstance

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_car_brands = CarBrand.objects.all().count()
    num_car_models = CarModel.objects.all().count()

    # The 'all()' is implied by default.
    # Available car_instances (status = 'a')
    num_car_instances_available  = CarModelInstance.objects.filter(status__exact='a').count()
     
    
    context = {
        'num_car_brands': num_car_brands,
        'num_car_models': num_car_models,
        'num_car_instances_available': num_car_instances_available,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)