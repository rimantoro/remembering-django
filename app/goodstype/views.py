from django.shortcuts import render
from rest_framework import viewsets
from .models import GoodsType
from .serializers import GoodsTypeSerializer
from .forms import GoodsTypeForm


def index(request):
    return render(request, 'goodstype/list.html')

# def detail(request):
#     form = GoodsTypeForm()
#     return render(request, 'goodstype/form.html', { 'form': form })


class GoodstypeViewSet(viewsets.ModelViewSet):
    queryset = GoodsType.objects.all().order_by('id')
    serializer_class = GoodsTypeSerializer