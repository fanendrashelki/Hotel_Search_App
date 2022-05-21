from multiprocessing import context
from posixpath import split
from django.shortcuts import render
from app.models import Emenities, hotel
from django.http import JsonResponse
# Create your views here.


def home(request):
    emenities = Emenities.objects.all()
    context = {'emenities': emenities}
    return render(request, 'index.html', context)


def api_hotel(request):
    hotels_objs = hotel.objects.all()
    price = request.GET.get('price')
    if price:
        hotels_objs = hotels_objs.filter(price__lte=price)

    emenities = request.GET.get('emenities')
    if emenities:
        emenities = emenities.split(',')
        em = []
        for e in emenities:
            try:
                em.append(int(e))
            except Exception as e:
                pass

        hotels_objs = hotels_objs.filter(emenities__in=em).distinct()

    payload = []
    for hotel_obj in hotels_objs:
        result = {}
        result['hotel_name'] = hotel_obj.hotel_name
        result['hotel_description'] = hotel_obj.hotel_description
        result['hotel_images'] = hotel_obj.hotel_images
        result['hotel_price'] = hotel_obj.price

        payload.append(result)

    return JsonResponse(payload, safe=False)


