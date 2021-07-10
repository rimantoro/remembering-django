# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import GoodsType

class GoodsTypeAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('goods_type', 'temp_min', 'temp_max')
    list_filter = ('goods_type',)
    fieldsets = (
        (None, {'fields': ('goods_type')}),
        ('Temperature Threshold', {'fields': ( 'temp_min', 'temp_max' )}),
    )
    # # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2')}
    #     ),
    # )
    search_fields = ('goods_type', 'temp_min', 'temp_max')
    ordering = ('goods_type',)
    filter_horizontal = ()


admin.site.register(GoodsType, GoodsTypeAdmin)
