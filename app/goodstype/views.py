import logging
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets
from .models import GoodsType
from .serializers import GoodsTypeSerializer
from .forms import GoodsTypeForm


def index(request):
    return render(request, 'goodstype/list.html')

def detail(request, id=None):
    context = {
        'msg': None,
        'success': None,
        'segment': None,
        'form': None,
    }

    if request.method == "POST":
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
            return redirect("/gstypes/")
    else:
        context['form'] = GoodsTypeForm()
    
    context['segment'] = request.path.split('/')[-1]
    html_template = loader.get_template( 'goodstype/form.html' )
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