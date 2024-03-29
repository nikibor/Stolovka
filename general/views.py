import random

from faker import Faker
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Place
from .serializers import MapSerializer


def is_point_in_area(left_top_long, left_top_lan,
                     right_bot_long, right_bot_lan,
                     place_long, place_lan):
    if left_top_long > place_long > right_bot_long \
            and left_top_lan > place_lan > right_bot_lan:
        return True
    else:
        return False


class Map(APIView):

    def get(self, request, format=None):
        fake = Faker('ru_RU')
        for i in range(100):
            title = fake.company()
            rating = random.randint(1, 5)
            longitude = 30.315868 + random.randrange(1, 99999) / 1000000
            latitude = 59.939095 + random.randrange(1, 99999) / 1000000
            place = Place(
                latitude=latitude,
                longitude=longitude,
                title=title,
                rating=rating
            )
            place.save()
        return Response(status=200)

    def post(self, request, format=None):
        serializer = MapSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data='qwerty', status=400)

        y1 = serializer.data['left_top_longitude']
        x1 = serializer.data['left_top_latitude']
        y2 = serializer.data['right_bottom_longitude']
        x2 = serializer.data['right_bottom_longitude']

        all_places = Place.objects.all()
        places = []
        for place in all_places:
            if is_point_in_area(x1, y1, x2, y2, float(place.latitude), float(place.longitude)):
                places.append({
                    'id': place.id,
                    'longitude': float(place.longitude),
                    'latitude': float(place.latitude),
                    'title': place.title,
                    'raiting': float(place.rating)
                })

        return Response(data={
            'places': places
        }, status=200)
