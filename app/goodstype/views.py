from django.shortcuts import render
from rest_framework import viewsets
from .models import GoodsType
from .serializers import GoodsTypeSerializer


def index(request):
    return render(request, 'goodstype/list.html')


class GoodstypeViewSet(viewsets.ModelViewSet):
    queryset = GoodsType.objects.all().order_by('id')
    serializer_class = GoodsTypeSerializer