from django.contrib import admin

from api_yamdb.admin import BaseAdmin
from user.models import User


@admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = (
        'username',
        'email',
        'role',
        'bio',
        'first_name',
        'last_name',
    )
    search_fields = (
        'username',
        'role',
    )
    list_filter = ('username',)
