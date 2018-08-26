from django.shortcuts import render

from .models import Name
# Create your views here.


def name(request):

    names = Name.objects.all()

    context = {
            'fullname': names[0].getfullname(),
        }
    return render(request, 'name.html', context=context)
