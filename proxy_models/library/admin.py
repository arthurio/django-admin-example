from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class AuthorAdmin(UserAdmin):
    search_fields = (
        'username',
        'email',
    )


class BookAdmin(admin.ModelAdmin):
    autocomplete_fields = (
        'author',
    )


# Register your models here.
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)
