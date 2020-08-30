from django.shortcuts import render

from .models import listing_model
from django.http import JsonResponse


def home(request):
    all_detail = listing_model.objects.all()
    print(all_detail)
    return render(request, 'index.html', context={'tasks': all_detail})


# ajax
def contact(request, id):
    numbers = listing_model.objects.get(id=id)
    return JsonResponse({'numbers': numbers.phone})
