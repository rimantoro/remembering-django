import logging
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseServerError
from rest_framework import viewsets
from .models import GoodsType
from .serializers import GoodsTypeSerializer
from .forms import GoodsTypeForm


def index(request):
    return render(request, 'goodstype/list.html')

def create(request):
    context = {
        'msg': None,
        'success': None,
        'segment': None,
        'form': None,
    }
    html_template = loader.get_template( 'goodstype/form.html' )
    if request.method == "POST":
        id = request.POST.get('id')
        form = GoodsTypeForm(request.POST)
        if form.is_valid():
            myform = form.save()
            logging.error('call form.save(), result=%s', myform)
            context['msg']     = 'data created.'
            context['success'] = True
            return redirect("/gstypes/")
        else:
            context['msg'] = 'Form is not valid'
            context['success'] = False 
    context['form'] = GoodsTypeForm()
    context['segment'] = request.path.split('/')[-1]
    return HttpResponse(html_template.render(context, request))

def change(request, id):
    context = {
        'msg': None,
        'success': None,
        'segment': None,
        'form': None,
        'id': id,
    }
    try:
        html_template = loader.get_template( 'goodstype/form.html' )
        if request.method == "POST":
            id = request.POST.get('id')
            item = GoodsType.objects.get(id=id)
            item.goods_type = request.POST.get('goods_type')
            item.temp_min = request.POST.get('temp_min')
            item.temp_max = request.POST.get('temp_max')
            item.save()
            logging.error('call item.save(), result=%s', item)
            context['msg']     = 'data created.'
            context['success'] = True
            return redirect("/gstypes/")
    except Exception as e:
        context['msg'] = 'Form is not valid'
        context['success'] = False
        messages.error(request, print(e))

    item = GoodsType.objects.get(pk=id)
    context['form'] = GoodsTypeForm(instance=item)
    context['segment'] = request.path.split('/')[-1]
    return HttpResponse(html_template.render(context, request))

def do_delete(request):
    context = {
        'msg': None,
        'success': None,
        'segment': None
    }
    try:
        if request.method == "POST":
            id = request.POST.get('id', False)
            obj = GoodsType.objects.get(pk=id)
            obj.delete()
            context['msg'] = 'deleted'
            context['success'] = True
        return redirect("/gstypes/")
    except (RuntimeError, TypeError, NameError):
        logging.error('ERROR', runtime=RuntimeError, typeerr=TypeError, nameerr=NameError)
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
    


class GoodstypeViewSet(viewsets.ModelViewSet):
    queryset = GoodsType.objects.all().order_by('id')
    serializer_class = GoodsTypeSerializer