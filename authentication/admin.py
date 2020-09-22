# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

# class UserGroupAdmin(admin.ModelAdmin):
#     pass

# class UserGroupInline(admin.StackedInline):
#     model = User
#     filter_horizontal = ('groups',)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'admin', 'last_login')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'last_login')}),
        ('Personal info', {'fields': ( 'first_name', 'last_name' )}),
        ('Permissions', {'fields': ('admin','groups',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'username', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

    # inlines = [UserGroupInline]


admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)
# admin.site.register(Group)
