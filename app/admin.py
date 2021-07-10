# -*- encoding: utf-8 -*-


from django.contrib import admin

from app.goodstype.models import GoodsType

class GoodsTypeAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'goods_type', 'temp_min', 'temp_max')
    list_filter = ('goods_type',)
    fieldsets = (
        (None, {'fields': ('id', 'goods_type')}),
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
    ordering = ('id',)
    filter_horizontal = ()


admin.site.register(GoodsType, GoodsTypeAdmin)