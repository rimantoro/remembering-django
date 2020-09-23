# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from app.goodstype import views as vw_goodstype

router = routers.DefaultRouter()
router.register(r'gstype', vw_goodstype.GoodstypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^api/', include(router.urls)),

    path('gstype/', vw_goodstype.index, name='goodstypes'),

    path('accounts/', include('allauth.urls')),
    path("", include("authentication.urls")),
    path("", include("app.urls")),
]
