from rest_framework.views import APIView
from rest_framework.response import Response

from apps.base.models import FoodCategory, Food
from apps.base.serializers import FoodListSerializer

from django.db.models import Prefetch


class FoodsListAPIView(APIView):

    def get(self, request):
        query = FoodCategory.objects.filter(food__is_publish=True)\
            .prefetch_related(
            Prefetch("food",
                     queryset=Food.objects.filter(is_publish=True))).distinct()
        serializer = FoodListSerializer(query, many=True)
        return Response(serializer.data)
